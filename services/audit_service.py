from models.audit import AuditLog
def audit(db, user_id, action, entity, record_id=None, result="Success", details=None, old_value=None, new_value=None, ip_address=None):
    db.add(AuditLog(user_id=user_id, action=action, entity_name=entity, record_id=str(record_id) if record_id else None, result=result, details=details, old_value=old_value, new_value=new_value, ip_address=ip_address))
    db.commit()
