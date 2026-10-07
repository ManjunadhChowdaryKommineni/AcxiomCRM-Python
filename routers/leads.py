from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from models.lead import Lead
from services.audit_service import audit
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
router=APIRouter(prefix="/leads",tags=["Leads"])
STATUSES=["New","Contacted","Qualified","Unqualified","Converted","Lost"]
@router.get("")
def leads(request:Request,q:str="",db:Session=Depends(get_db)):
    if not request.session.get("user_id"): return RedirectResponse("/login",303)
    query=db.query(Lead)
    if q: query=query.filter(Lead.lead_name.ilike(f"%{q}%") | Lead.email.ilike(f"%{q}%"))
    return templates.TemplateResponse("leads/list.html", {"request":request,"leads":query.order_by(Lead.id.desc()).all(),"statuses":STATUSES,"q":q})
@router.post("/create")
def create(request:Request,lead_name:str=Form(...),email:str=Form(...),phone:str=Form(...),company_name:str=Form(""),source:str=Form("Website"),status:str=Form("New"),priority:str=Form("Medium"),expected_value:float=Form(0),db:Session=Depends(get_db)):
    uid=request.session.get("user_id")
    if not uid:return RedirectResponse("/login",303)
    if status not in STATUSES or expected_value<0:return RedirectResponse("/leads",303)
    code=f"LEAD-{db.query(Lead).count()+1:04d}"; x=Lead(lead_code=code,lead_name=lead_name,email=email.lower(),phone=phone,company_name=company_name,source=source,status=status,priority=priority,expected_value=expected_value,assigned_to=uid)
    db.add(x); db.commit(); db.refresh(x); audit(db,uid,"CREATE","Lead",x.id); return RedirectResponse("/leads",303)
