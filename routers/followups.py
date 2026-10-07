from datetime import date
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from models.followup import FollowUp
from services.audit_service import audit
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
router=APIRouter(prefix="/followups",tags=["Follow-ups"])
@router.get("")
def followups(request:Request,db:Session=Depends(get_db)):
    if not request.session.get("user_id"): return RedirectResponse("/login",303)
    return templates.TemplateResponse("followups/list.html", {"request":request,"followups":db.query(FollowUp).order_by(FollowUp.follow_up_date).all()})
@router.post("/create")
def create(request:Request,follow_up_date:date=Form(...),follow_up_type:str=Form("Call"),subject:str=Form(...),remarks:str=Form(""),db:Session=Depends(get_db)):
    uid=request.session.get("user_id")
    if not uid:return RedirectResponse("/login",303)
    if follow_up_date<date.today(): return RedirectResponse("/followups",303)
    x=FollowUp(follow_up_date=follow_up_date,follow_up_type=follow_up_type,subject=subject,remarks=remarks,assigned_to=uid)
    db.add(x); db.commit(); db.refresh(x); audit(db,uid,"CREATE","FollowUp",x.id); return RedirectResponse("/followups",303)
