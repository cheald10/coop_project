# COOP Platform — Deployment Guide
## PythonAnywhere + GitHub

---

## Overview

This guide walks you through deploying the COOP platform to:
- **GitHub**: https://github.com/cheald10/coop_project (source control)
- **PythonAnywhere**: https://bcp-dev.pythonanywhere.com (live app)

---

## STEP 1 — Push to GitHub (do this on your local machine)

### 1a. Initialize the repo locally
```bash
cd coop_project          # the project root folder
git init
git remote add origin https://github.com/cheald10/coop_project.git
```

### 1b. Stage and commit everything
```bash
git add .
git commit -m "Initial commit — fixed all critical issues, ready for deployment"
git branch -M main
git push -u origin main
```

> If the repo doesn't exist yet, create it at https://github.com/new (name: coop_project, private recommended).

---

## STEP 2 — PythonAnywhere Setup

### 2a. Create a MySQL database
1. Log in at https://www.pythonanywhere.com
2. Go to **Databases** tab
3. Create a database named: `coopdb`  
   Full name will be: `bcp_dev$coopdb`
4. Note your MySQL password

### 2b. Open a Bash console on PythonAnywhere
Go to **Consoles → Bash**

### 2c. Clone your repo
```bash
cd ~
git clone https://github.com/cheald10/coop_project.git
cd coop_project
```

### 2d. Create and activate a virtualenv
```bash
mkvirtualenv --python=/usr/bin/python3.10 coopenv
# (virtualenv activates automatically)
pip install -r requirements.txt
```

> If mysqlclient fails to install, try: `pip install mysqlclient --no-binary mysqlclient`

### 2e. Create your .env file
```bash
cp .env.example .env
nano .env      # fill in your actual values
```

Key values to set:
```
SECRET_KEY=<generate one at https://djecrety.ir/>
DEBUG=False
DB_PASSWORD=<your MySQL password from step 2a>
ALLOWED_HOSTS=bcp-dev.pythonanywhere.com
MEDIA_ROOT=/home/bcp_dev/coop_project/media
```

### 2f. Run migrations
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

---

## STEP 3 — Configure the Web App on PythonAnywhere

1. Go to **Web** tab → **Add a new web app**
2. Choose **Manual configuration** (not Django wizard)
3. Choose **Python 3.10**

### 3a. Set the source code directory
```
/home/bcp_dev/coop_project
```

### 3b. Set the virtualenv path
```
/home/bcp_dev/.virtualenvs/coopenv
```

### 3c. Edit the WSGI configuration file
Click the WSGI file link (something like `/var/www/bcp_dev_pythonanywhere_com_wsgi.py`)

Replace ALL contents with:
```python
import os
import sys

path = '/home/bcp_dev/coop_project'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'coop_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 3d. Set static files mapping
In the **Static files** section:
| URL         | Directory                                    |
|-------------|----------------------------------------------|
| `/static/`  | `/home/bcp_dev/coop_project/staticfiles`     |
| `/media/`   | `/home/bcp_dev/coop_project/media`           |

### 3e. Reload the web app
Click the green **Reload** button.

---

## STEP 4 — Verify Deployment

Visit: https://bcp-dev.pythonanywhere.com

You should see the login page. Log in with the superuser you created.

### Quick smoke test checklist:
- [ ] Login page loads
- [ ] Division list loads after login
- [ ] Create a test division (via Django admin at `/admin/`)
- [ ] Navigate to all 9 section lists
- [ ] Try adding a record to each section
- [ ] Generate a COOP plan
- [ ] Leadership dashboard loads at `/dashboard/leadership/`
- [ ] REST API at `/api/v1/` requires authentication

---

## STEP 5 — Ongoing Workflow (after initial deploy)

Every time you make changes:

**On your local machine:**
```bash
# Make changes to files...
git add .
git commit -m "Description of changes"
git push origin main
```

**On PythonAnywhere (Bash console):**
```bash
cd ~/coop_project
git pull origin main
python manage.py migrate          # only if models changed
python manage.py collectstatic --noinput   # only if static files changed
# Then reload the web app from the Web tab
```

---

## STEP 6 — First-Time Data Setup

After deployment, do this via Django Admin (`/admin/`):

1. **Create Groups**: COOP Admins, Coordinators, Leadership
2. **Create Divisions** (or import from CSV)
3. **Create DivisionMetadata** for each division
4. **Assign coordinators** to divisions
5. **Assign users** to appropriate groups

---

## Troubleshooting

### App won't start / 500 error
Check the error log in PythonAnywhere Web tab → Error log

### Database connection error
- Verify DB_HOST matches: `bcp-dev.mysql.pythonanywhere-services.com`
- Confirm DB_NAME format: `bcp_dev$coopdb`

### Static files not loading
Run `python manage.py collectstatic --noinput` and check the static files mapping

### Import errors
Make sure your virtualenv is active and all packages installed:
```bash
workon coopenv
pip install -r requirements.txt
```

### mysqlclient install fails
```bash
pip install mysqlclient --no-binary mysqlclient
# OR use PyMySQL as fallback:
pip install PyMySQL
# Then add to coop_project/__init__.py:
# import pymysql; pymysql.install_as_MySQLdb()
```
