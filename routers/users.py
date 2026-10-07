from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from services.auth_service import hash_password
from services.audit_service import audit
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
router=APIRouter(prefix="/users",tags=["Users"])
@router.get("")
def users(request:Request,db:Session=Depends(get_db)):
    if not request.session.get("user_id") or request.session.get("role")!="Admin": return RedirectResponse("/dashboard",303)
    return templates.TemplateResponse("users/list.html", {"request":request,"users":db.query(User).order_by(User.id).all()})
@router.post("/create")
def create(request:Request,name:str=Form(...),email:str=Form(...),password:str=Form(...),role:str=Form("SalesExecutive"),db:Session=Depends(get_db)):
    if request.session.get("role")!="Admin":return RedirectResponse("/dashboard",303)
    if role not in ["Admin","Manager","SalesExecutive"] or db.query(User).filter(User.email==email.lower()).first():return RedirectResponse("/users",303)
    u=User(name=name,email=email.lower(),password_hash=hash_password(password),role=role);db.add(u);db.commit();db.refresh(u);audit(db,request.session["user_id"],"CREATE","User",u.id);return RedirectResponse("/users",303)
