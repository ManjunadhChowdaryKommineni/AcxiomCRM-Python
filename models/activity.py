from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
from database import Base
class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    activity_type = Column(String(30), nullable=False)
    subject = Column(String(150), nullable=False)
    description = Column(Text)
    activity_date = Column(Date, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    lead_id = Column(Integer, ForeignKey("leads.id"))
    assigned_to = Column(Integer, ForeignKey("users.id"))
    status = Column(String(30), nullable=False, default="Planned")
