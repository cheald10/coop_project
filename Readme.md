# COOP Continuity Planning Platform  
### Developed by **Heald & Heritage LLC** using Microsoft Copilot

A full‑stack Continuity of Operations (COOP) planning system built with **Django**, **PostgreSQL**, and a clean **HTML template–based UI**.  
This platform enables organizations to build, maintain, and generate complete COOP plans across multiple divisions with structured data, automated document generation, and role‑based access control.

---

## 📘 Overview

The COOP Continuity Planning Platform replaces fragmented spreadsheets, SharePoint lists, and manual Word templates with a unified, secure, and automated system.

### **Core Capabilities**
- **Division‑based COOP plan management**  
- **Automated Word + PDF COOP plan generation**  
- **Role‑based access control (Admin, Coordinator, Leadership)**  
- **Bootstrap‑styled HTML template frontend**  
- **Centralized PostgreSQL data model**  
- **Leadership readiness dashboard**  
- **SharePoint CSV migration support**  
- **Versioned plan history and auditability**

---

# 🚀 Quick Start Guide

This guide helps you run the platform locally on your personal machine.

---

## Prerequisites

### System Requirements
- Python 3.10+
- PostgreSQL 14+
- Git
- pip / venv
- LibreOffice (for DOCX → PDF conversion)
- Windows, macOS, or Linux

### Python Dependencies  
Installed via `requirements.txt`:
- Django  
- Django REST Framework  
- python-docx  
- docx2pdf  
- psycopg2  

---

# 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-org>/<your-repo>.git
cd <your-repo>
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables  
Create a `.env` file in the project root:

```bash
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_NAME=coopdb
DATABASE_USER=postgres
DATABASE_PASSWORD=yourpassword
DATABASE_HOST=localhost
DATABASE_PORT=5432
MEDIA_ROOT=media
MEDIA_URL=/media/
```

### 5. Create the PostgreSQL database
```sql
CREATE DATABASE coopdb;
```

### 6. Run migrations
```bash
python manage.py migrate
```

### 7. Create a superuser
```bash
python manage.py createsuperuser
```

### 8. Start the development server
```bash
python manage.py runserver
```

### Visit:
```
http://127.0.0.1:8000
```
```

# 🔧 Environment Variables

Create a `.env` file in the project root with the following values:



```
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_NAME=coopdb
DATABASE_USER=postgres
DATABASE_PASSWORD=yourpassword
DATABASE_HOST=localhost
DATABASE_PORT=5432
MEDIA_ROOT=media
MEDIA_URL=/media/
```

---

# 📁 Project Structure

```
project_root/
│
├── app/
│   ├── models.py               # All 10 COOP data models
│   ├── views.py                # Full CRUD + plan generation
│   ├── forms.py                # ModelForms for all lists
│   ├── middleware.py           # Role-based permission middleware
│   ├── services/
│   │   └── coop_plan.py        # Word/PDF generation engine
│   ├── management/
│   │   └── commands/
│   │       └── import_sharepoint.py  # CSV migration script
│   ├── templates/
│   │   ├── base.html
│   │   ├── includes/
│   │   ├── divisions/
│   │   ├── essential_functions/
│   │   ├── critical_applications/
│   │   ├── key_personnel/
│   │   ├── vital_records/
│   │   ├── dependencies/
│   │   ├── alternate_facilities/
│   │   ├── communications/
│   │   ├── recovery_priorities/
│   │   ├── division_metadata/
│   │   └── coop_plan/
│   └── urls.py
│
├── coop_project/
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Global URL routing
│   └── wsgi.py
│
├── media/                      # Generated Word/PDF files
├── data/                       # SharePoint CSV imports
├── requirements.txt
└── README.md
```

---

# ⭐ Key Features

### **1. Division‑Scoped COOP Management**
Each division maintains:
- Essential Functions  
- Critical Applications  
- Key Personnel  
- Vital Records  
- Dependencies  
- Alternate Facilities  
- Communications  
- Recovery Priorities  
- Division Metadata  

### **2. Automated COOP Plan Generation**
- Pulls all division data  
- Populates a Word template  
- Converts to PDF  
- Saves both files  
- Increments version number  
- Logs history  

### **3. Role‑Based Access Control**
| Role | Capabilities |
|------|--------------|
| **Admin** | Full access to all divisions |
| **Coordinator** | Edit only their division |
| **Leadership** | Read‑only + dashboard |

### **4. Leadership Dashboard**
- Division readiness overview  
- Plan version tracking  
- Essential function counts  
- Critical application counts  

### **5. SharePoint Migration Script**
Imports CSV exports from:
- Essential Functions  
- Critical Applications  
- Key Personnel  
- Vital Records  
- Dependencies  
- Alternate Facilities  
- Communications  
- Recovery Priorities  
- Division Metadata  
- Divisions  

### **6. Clean HTML Template Frontend**
- Bootstrap UI  
- Sidebar navigation  
- Division‑aware context processor  
- No JavaScript framework required  

---

# 🏢 Developer Attribution

This platform was designed and developed by:

### **Heald & Heritage LLC**  
*Leveraging Microsoft Copilot for accelerated architecture, code generation, and documentation.*

If you use or extend this project, please retain attribution in your documentation.
```

---

If you want, I can also generate a **fully normalized README** with consistent heading levels throughout, or help you add badges, screenshots, or a project logo.
