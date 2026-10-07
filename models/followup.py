from datetime import datetime
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from database import Base
class FollowUp(Base):
    __tablename__ = "followups"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    lead_id = Column(Integer, ForeignKey("leads.id"))
    opportunity_id = Column(Integer, ForeignKey("opportunities.id"))
    follow_up_date = Column(Date, nullable=False)
    follow_up_type = Column(String(30), nullable=False, default="Call")
    subject = Column(String(150), nullable=False)
    remarks = Column(String(500))
    status = Column(String(30), nullable=False, default="Planned")
    assigned_to = Column(Integer, ForeignKey("users.id"))
    created_date = Column(DateTime, default=datetime.utcnow, nullable=False)
