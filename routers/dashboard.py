from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from services.dashboard_service import metrics
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
router=APIRouter()
@router.get("/dashboard")
def dashboard(request:Request,db:Session=Depends(get_db)):
    if not request.session.get("user_id"): return RedirectResponse("/login",303)
    return templates.TemplateResponse("dashboard.html", {"request":request,"metrics":metrics(db),"role":request.session.get("role")})
