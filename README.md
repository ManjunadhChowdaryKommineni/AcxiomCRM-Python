# AcxiomCRM - Python/FastAPI

A deadline-focused CRM implementation based on the supplied AcxiomCRM specification, using Python, FastAPI, SQLAlchemy, SQLite, Jinja2, Bootstrap and Chart.js.

## Run in PowerShell

```powershell
cd C:\Users\manju\Downloads\AcxiomCRM-Python
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Then open http://127.0.0.1:8000

For auto-reload development:
```powershell
uvicorn main:app --reload
```

## Demo admin
- Email: `admin@acxiomcrm.local`
- Password: `Admin@123`

## API
- GET `/api/customers`
- GET `/api/leads`
- GET `/api/opportunities`
- Swagger: `/docs`

## Main implemented areas
Authentication/register/login/logout, password hashing, lockout, roles, dashboard KPIs/chart, customer CRUD create/search, leads, opportunities and weighted pipeline, follow-ups, activities, user/role management, audit logs, REST API, server-side validation and role checks.

## Important
This is an assignment/demo implementation. For production deployment, use HTTPS, a strong secret, CSRF protection for browser forms, migrations, stronger authorization scoping, secure cookie settings and a production database.
