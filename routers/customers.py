from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from models.customer import Customer
from services.audit_service import audit
import re
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
router=APIRouter(prefix="/customers",tags=["Customers"])
def guard(request): return request.session.get("user_id")
@router.get("")
def customers(request:Request,q:str="",db:Session=Depends(get_db)):
    if not guard(request): return RedirectResponse("/login",303)
    query=db.query(Customer)
    if q: query=query.filter(Customer.customer_name.ilike(f"%{q}%") | Customer.email.ilike(f"%{q}%") | Customer.phone.ilike(f"%{q}%"))
    return templates.TemplateResponse("customers/list.html", {"request":request,"customers":query.order_by(Customer.id.desc()).all(),"q":q})
@router.post("/create")
def create(request:Request,customer_name:str=Form(...),email:str=Form(...),phone:str=Form(...),company_name:str=Form(...),address:str=Form(""),city:str=Form(""),state:str=Form(""),db:Session=Depends(get_db)):
    uid=guard(request)
    if not uid:return RedirectResponse("/login",303)
    if not re.fullmatch(r"[0-9+() -]{7,20}",phone): return RedirectResponse("/customers?error=Invalid+phone",303)
    if db.query(Customer).filter((Customer.email==email.lower()) | (Customer.phone==phone)).first(): return RedirectResponse("/customers?error=Duplicate+email+or+phone",303)
    code=f"CUS-{db.query(Customer).count()+1:04d}"; c=Customer(customer_code=code,customer_name=customer_name,email=email.lower(),phone=phone,company_name=company_name,address=address,city=city,state=state,created_by=uid)
    db.add(c); db.commit(); db.refresh(c); audit(db,uid,"CREATE","Customer",c.id)
    return RedirectResponse("/customers",303)
@router.post("/{cid}/delete")
def delete(cid:int,request:Request,db:Session=Depends(get_db)):
    uid=guard(request)
    if not uid:return RedirectResponse("/login",303)
    if request.session.get("role")!="Admin": return RedirectResponse("/customers?error=Unauthorized",303)
    c=db.get(Customer,cid)
    if c: db.delete(c); db.commit(); audit(db,uid,"DELETE","Customer",cid)
    return RedirectResponse("/customers",303)
