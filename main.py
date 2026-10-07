from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from config import settings
from database import Base, engine, SessionLocal
import models
from models.user import User
from services.auth_service import hash_password
from routers import auth, dashboard, customers, leads, opportunities, followups, activities, users, audit, api

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    description="Python CRM assignment implementation"
)

app.add_middleware(
    SessionMiddleware,
    secret_key=settings.secret_key,
    session_cookie=settings.session_cookie,
    max_age=60 * 60 * 8,
    https_only=False,
    same_site="lax"
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

for r in [
    auth.router,
    dashboard.router,
    customers.router,
    leads.router,
    opportunities.router,
    followups.router,
    activities.router,
    users.router,
    audit.router,
    api.router
]:
    app.include_router(r)


@app.get("/")
def root():
    from fastapi.responses import RedirectResponse
    return RedirectResponse("/dashboard", 303)


@app.on_event("startup")
def seed_users():
    db = SessionLocal()

    try:
        demo_users = [
            (
                "System Admin",
                "admin@acxiomcrm.local",
                "Admin@123",
                "Admin"
            ),
            (
                "CRM Manager",
                "manager@acxiomcrm.local",
                "Manager@123",
                "Manager"
            ),
            (
                "Sales Executive 1",
                "sales1@acxiomcrm.local",
                "Sales@123",
                "SalesExecutive"
            ),
            (
                "Sales Executive 2",
                "sales2@acxiomcrm.local",
                "Sales@123",
                "SalesExecutive"
            )
        ]

        for name, email, password, role in demo_users:
            existing = db.query(User).filter(
                User.email == email
            ).first()

            if not existing:
                user = User(
                    name=name,
                    email=email,
                    password_hash=hash_password(password),
                    role=role
                )
                db.add(user)

        db.commit()

    finally:
        db.close()
