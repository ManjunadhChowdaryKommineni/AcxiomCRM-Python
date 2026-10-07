from datetime import datetime, timedelta
from passlib.context import CryptContext
from config import settings
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password): return pwd_context.hash(password)
def verify_password(password, hashed): return pwd_context.verify(password, hashed)
def locked(user): return bool(user.lockout_end and user.lockout_end > datetime.utcnow())
def register_failure(user):
    user.failed_login_count += 1
    if user.failed_login_count >= settings.max_login_attempts:
        user.lockout_end = datetime.utcnow() + timedelta(minutes=settings.lockout_minutes)
        user.failed_login_count = 0

def reset_failures(user):
    user.failed_login_count = 0
    user.lockout_end = None
