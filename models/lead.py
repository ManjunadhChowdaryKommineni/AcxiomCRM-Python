from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from database import Base
class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    lead_code = Column(String(30), unique=True, nullable=False, index=True)
    lead_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(20), nullable=False)
    company_name = Column(String(150))
    source = Column(String(50), nullable=False, default="Website")
    status = Column(String(30), nullable=False, default="New")
    priority = Column(String(20), nullable=False, default="Medium")
    expected_value = Column(Numeric(12, 2), default=0, nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    assigned_to = Column(Integer, ForeignKey("users.id"))
