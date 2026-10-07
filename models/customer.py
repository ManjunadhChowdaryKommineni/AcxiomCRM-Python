from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from database import Base
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    customer_code = Column(String(30), unique=True, nullable=False, index=True)
    customer_name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    phone = Column(String(20), unique=True, nullable=False)
    company_name = Column(String(150), nullable=False)
    address = Column(String(250))
    city = Column(String(100))
    state = Column(String(100))
    status = Column(String(30), default="Active", nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"))
