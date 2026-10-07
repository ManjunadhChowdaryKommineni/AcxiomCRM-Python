from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from database import Base
class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String(50), nullable=False)
    entity_name = Column(String(100), nullable=False)
    record_id = Column(String(50))
    old_value = Column(Text)
    new_value = Column(Text)
    created_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    ip_address = Column(String(50))
    result = Column(String(30), nullable=False, default="Success")
    details = Column(Text)
