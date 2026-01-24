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
