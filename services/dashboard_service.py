from sqlalchemy import func
from models.customer import Customer
from models.lead import Lead
from models.opportunity import Opportunity
def metrics(db):
    return {
      "customers": db.query(Customer).count(),
      "leads": db.query(Lead).count(),
      "open_leads": db.query(Lead).filter(Lead.status.in_(["New","Contacted","Qualified"])).count(),
      "opportunities": db.query(Opportunity).count(),
      "open_opportunities": db.query(Opportunity).filter(Opportunity.status=="Open").count(),
      "won": db.query(Opportunity).filter(Opportunity.stage=="Won").count(),
      "lost": db.query(Opportunity).filter(Opportunity.stage=="Lost").count(),
      "pipeline": float(db.query(func.coalesce(func.sum(Opportunity.amount * Opportunity.probability / 100),0)).scalar() or 0),
    }
