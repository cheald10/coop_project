# BCP-Dev-Tool
COOP Continuity Planning Platform
Developed by Heald & Heritage LLC using Microsoft Copilot
A full‑stack Continuity of Operations (COOP) planning system built with Django, PostgreSQL, and HTML template–based UI.
This platform enables organizations to build, maintain, and generate complete COOP plans across multiple divisions with structured data, automated document generation, and role‑based access control.

📘 Overview
The COOP Continuity Planning Platform is designed to replace fragmented spreadsheets, SharePoint lists, and manual Word templates with a unified, secure, and automated system.

Core Capabilities
Division‑based COOP plan management  
Each division maintains its own essential functions, applications, personnel, and dependencies.

Automated COOP plan generation  
Generates a complete Word + PDF COOP plan using a structured template and division data.

Role‑based access control  
Admins, Coordinators, and Leadership each have tailored permissions.

HTML template frontend 
Clean, fast, server‑rendered UI with Bootstrap styling.

Centralized data model  
Ten interconnected lists (Essential Functions, Critical Applications, etc.) stored in PostgreSQL.

Leadership dashboard  
High‑level readiness overview across all divisions.

SharePoint migration support  
Import scripts for CSV exports from legacy SharePoint COOP systems.

Audit‑friendly versioning  
Each generated plan increments the division’s version number and stores historical outputs.

🚀 Quick Start Guide
This guide helps you run the platform locally on your personal machine.

Prerequisites
Make sure you have the following installed:

System Requirements
Python 3.10+

PostgreSQL 14+

pip / venv

Git

LibreOffice (for DOCX → PDF conversion)

Windows, macOS, or Linux

Python Dependencies
These will be installed automatically via requirements.txt:

Django

Django REST Framework

python-docx

docx2pdf

psycopg2

Bootstrap (via CDN)
