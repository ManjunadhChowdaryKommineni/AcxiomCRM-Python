from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from models.audit import AuditLog
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
router=APIRouter(prefix="/audit",tags=["Audit"])
@router.get("")
def audit_logs(request:Request,db:Session=Depends(get_db)):
    if not request.session.get("user_id") or request.session.get("role") not in ["Admin","Manager"]: return RedirectResponse("/dashboard",303)
    return templates.TemplateResponse("audit/list.html", {"request":request,"logs":db.query(AuditLog).order_by(AuditLog.id.desc()).limit(300).all()})
