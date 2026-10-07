from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from database import get_db
from models.customer import Customer
router=APIRouter(prefix="/api",tags=["REST API"])
def auth(request:Request):
    if not request.session.get("user_id"): raise HTTPException(401,"Authentication required")
    return request.session["user_id"]
@router.get("/customers")
def api_customers(request:Request,db:Session=Depends(get_db),uid=Depends(auth)):
    rows=db.query(Customer).order_by(Customer.id.desc()).all()
    return [{"id":x.id,"customer_code":x.customer_code,"customer_name":x.customer_name,"email":x.email,"phone":x.phone,"company_name":x.company_name,"status":x.status} for x in rows]
@router.get("/leads")
def api_leads(request:Request,db:Session=Depends(get_db),uid=Depends(auth)):
    from models.lead import Lead
    rows=db.query(Lead).order_by(Lead.id.desc()).all()
    return [{"id":x.id,"lead_code":x.lead_code,"lead_name":x.lead_name,"email":x.email,"phone":x.phone,"status":x.status,"expected_value":float(x.expected_value or 0)} for x in rows]
@router.get("/opportunities")
def api_opportunities(request:Request,db:Session=Depends(get_db),uid=Depends(auth)):
    from models.opportunity import Opportunity
    rows=db.query(Opportunity).order_by(Opportunity.id.desc()).all()
    return [{"id":x.id,"name":x.opportunity_name,"amount":float(x.amount),"stage":x.stage,"probability":x.probability,"weighted_pipeline":float(x.amount)*x.probability/100} for x in rows]
