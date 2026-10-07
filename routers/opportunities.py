from datetime import date
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from models.opportunity import Opportunity
from services.audit_service import audit
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
router=APIRouter(prefix="/opportunities",tags=["Opportunities"])
STAGES=["Qualification","Proposal","Negotiation","Won","Lost"]
@router.get("")
def opportunities(request:Request,db:Session=Depends(get_db)):
    if not request.session.get("user_id"): return RedirectResponse("/login",303)
    return templates.TemplateResponse("opportunities/list.html", {"request":request,"opportunities":db.query(Opportunity).order_by(Opportunity.id.desc()).all(),"stages":STAGES})
@router.post("/create")
def create(request:Request,opportunity_name:str=Form(...),amount:float=Form(...),stage:str=Form("Qualification"),probability:int=Form(0),expected_close_date:date=Form(...),notes:str=Form(""),db:Session=Depends(get_db)):
    uid=request.session.get("user_id")
    if not uid:return RedirectResponse("/login",303)
    if amount<=0 or probability<0 or probability>100 or expected_close_date<date.today() or stage not in STAGES:return RedirectResponse("/opportunities",303)
    x=Opportunity(opportunity_name=opportunity_name,amount=amount,stage=stage,probability=probability,expected_close_date=expected_close_date,notes=notes,assigned_to=uid,status="Won" if stage=="Won" else "Lost" if stage=="Lost" else "Open")
    db.add(x); db.commit(); db.refresh(x); audit(db,uid,"CREATE","Opportunity",x.id); return RedirectResponse("/opportunities",303)
