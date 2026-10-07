# AcxiomCRM – Customer Relationship Management System

AcxiomCRM is a role-based Customer Relationship Management (CRM) web application developed using Python and FastAPI.

The system provides customer, lead, opportunity, follow-up, activity, user management, dashboard, REST API, and audit logging functionality.

---

## 🚀 Technology Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Jinja2
- Bootstrap
- Chart.js
- HTML
- CSS
- JavaScript
- REST API
- Role-Based Access Control (RBAC)
- Session-Based Authentication

---

## 📌 Main Features

### 🔐 Authentication & Authorization
- User Login
- User Registration
- Logout
- Password Hashing
- Session Management
- Login Failure Tracking
- Account Lockout
- Role-Based Access Control

### 📊 Dashboard
- Total Customers
- Total Leads
- Open Leads
- Total Opportunities
- Open Opportunities
- Won Opportunities
- Lost Opportunities
- Total Pipeline Value
- Lead Status Chart
- Opportunity Pipeline Chart
- Monthly Sales Chart

### 👥 Customer Management
- Add Customer
- View Customer
- Update Customer
- Delete Customer
- Search Customers
- Customer Status
- Duplicate Email Prevention
- Duplicate Phone Prevention

### 🎯 Lead Management
- Add Lead
- View Lead
- Update Lead
- Delete Lead
- Lead Status
- Lead Priority
- Lead Assignment
- Lead Conversion

### 💰 Opportunity Management
- Add Opportunity
- View Opportunity
- Update Opportunity
- Delete Opportunity
- Opportunity Stage
- Amount
- Probability
- Expected Close Date
- Weighted Pipeline Calculation

### 📅 Follow-Up Management
- Schedule Follow-Ups
- Update Follow-Ups
- Complete Follow-Ups
- Pending Follow-Ups
- Follow-Up Status
- Follow-Up Type
- Customer/Lead/Opportunity Association

### 📞 Activity Management
- Calls
- Meetings
- Emails
- Tasks
- Activity Status

### 👤 User & Role Management
- Create Users
- Update Users
- Activate/Deactivate Users
- Role Management
- Admin
- Manager
- Sales Executive

### 📋 Audit Logging
The system records important activities such as:

- Login
- Logout
- Create operations
- Update operations
- Delete operations
- User changes
- Role changes
- Security-related actions

---

# 🔑 Demo Login Credentials

These accounts are provided for **local development and project demonstration**.

| Role | ID / Email | Password |
|---|---|---|
| Admin | `admin@acxiomcrm.local` | `Admin@123` |
| Manager | `manager@acxiomcrm.local` | `Manager@123` |
| Sales Executive 1 | `sales1@acxiomcrm.local` | `Sales@123` |
| Sales Executive 2 | `sales2@acxiomcrm.local` | `Sales@123` |

### 👑 Admin

**ID:** `admin@acxiomcrm.local`

**Password:** `Admin@123`

**Role:** `Admin`

Admin has full access to the CRM system, including user management, role management, audit logs, dashboard, customers, leads, opportunities, follow-ups and activities.

---

### 👔 Manager

**ID:** `manager@acxiomcrm.local`

**Password:** `Manager@123`

**Role:** `Manager`

Manager has access to CRM and team/business-level management features.

---

### 💼 Sales Executive 1

**ID:** `sales1@acxiomcrm.local`

**Password:** `Sales@123`

**Role:** `SalesExecutive`

Sales Executive 1 can work with assigned CRM records, leads, opportunities, follow-ups and activities.

---

### 💼 Sales Executive 2

**ID:** `sales2@acxiomcrm.local`

**Password:** `Sales@123`

**Role:** `SalesExecutive`

Sales Executive 2 can work with assigned CRM records, leads, opportunities, follow-ups and activities.

---

# 🛠️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/ManjunadhChowdaryKommineni/AcxiomCRM-Python.git
