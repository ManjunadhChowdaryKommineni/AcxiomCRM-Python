from datetime import datetime
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, Numeric, String
from database import Base
class Opportunity(Base):
    __tablename__ = "opportunities"
    id = Column(Integer, primary_key=True, index=True)
    opportunity_name = Column(String(150), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    lead_id = Column(Integer, ForeignKey("leads.id"))
    amount = Column(Numeric(12, 2), nullable=False)
    stage = Column(String(30), nullable=False, default="Qualification")
    probability = Column(Integer, nullable=False, default=0)
    expected_close_date = Column(Date, nullable=False)
    status = Column(String(30), nullable=False, default="Open")
    created_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    assigned_to = Column(Integer, ForeignKey("users.id"))
    notes = Column(String(500))
