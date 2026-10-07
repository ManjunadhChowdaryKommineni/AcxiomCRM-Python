from datetime import date
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from models.activity import Activity
from services.audit_service import audit
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
router=APIRouter(prefix="/activities",tags=["Activities"])
@router.get("")
def activities(request:Request,db:Session=Depends(get_db)):
    if not request.session.get("user_id"): return RedirectResponse("/login",303)
    return templates.TemplateResponse("activities/list.html", {"request":request,"activities":db.query(Activity).order_by(Activity.activity_date.desc()).all()})
@router.post("/create")
def create(request:Request,activity_type:str=Form(...),subject:str=Form(...),activity_date:date=Form(...),description:str=Form(""),status:str=Form("Planned"),db:Session=Depends(get_db)):
    uid=request.session.get("user_id")
    if not uid:return RedirectResponse("/login",303)
    x=Activity(activity_type=activity_type,subject=subject,activity_date=activity_date,description=description,status=status,assigned_to=uid)
    db.add(x);db.commit();db.refresh(x);audit(db,uid,"CREATE","Activity",x.id);return RedirectResponse("/activities",303)
