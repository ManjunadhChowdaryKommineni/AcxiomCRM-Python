from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from services.auth_service import hash_password, verify_password, locked, register_failure, reset_failures
from services.audit_service import audit
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
router = APIRouter()

def login_page(request, error=None): return {"request": request, "error": error}
@router.get("/login")
def login_get(request: Request): return templates.TemplateResponse("login.html", login_page(request))
@router.post("/login")
def login_post(request: Request, email: str=Form(...), password: str=Form(...), db: Session=Depends(get_db)):
    user=db.query(User).filter(User.email==email.lower().strip()).first()
    if not user or not user.is_active:
        return templates.TemplateResponse("login.html", login_page(request,"Invalid email or password"))
    if locked(user): return templates.TemplateResponse("login.html", login_page(request,"Account temporarily locked. Try again later."))
    if not verify_password(password,user.password_hash):
        register_failure(user); db.commit()
        if user.failed_login_count == 0: audit(db,user.id,"LOGIN_FAILED","User",user.id,"Failed","Account lockout threshold reached")
        return templates.TemplateResponse("login.html", login_page(request,"Invalid email or password"))
    reset_failures(user); db.commit(); audit(db,user.id,"LOGIN_SUCCESS","User",user.id)
    request.session["user_id"]=user.id; request.session["role"]=user.role
    return RedirectResponse("/dashboard",status_code=303)
@router.get("/register")
def register_get(request: Request): return templates.TemplateResponse("register.html", {"request":request,"error":None})
@router.post("/register")
def register_post(request: Request,name:str=Form(...),email:str=Form(...),password:str=Form(...),db:Session=Depends(get_db)):
    email=email.lower().strip()
    if len(password)<8: return templates.TemplateResponse("register.html", {"request":request,"error":"Password must be at least 8 characters"})
    if db.query(User).filter(User.email==email).first(): return templates.TemplateResponse("register.html", {"request":request,"error":"Email already registered"})
    u=User(name=name.strip(),email=email,password_hash=hash_password(password),role="SalesExecutive")
    db.add(u); db.commit(); db.refresh(u); audit(db,u.id,"REGISTER","User",u.id)
    request.session["user_id"]=u.id; request.session["role"]=u.role
    return RedirectResponse("/dashboard",status_code=303)
@router.get("/logout")
def logout(request:Request,db:Session=Depends(get_db)):
    uid=request.session.get("user_id")
    if uid: audit(db,uid,"LOGOUT","User",uid)
    request.session.clear(); return RedirectResponse("/login",status_code=303)
