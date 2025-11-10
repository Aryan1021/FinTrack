# 🐍💰 finTrack

A Django-based personal finance tracking application. Perfect for managing income, expenses, setting financial goals, and monitoring savings progress.

---

## 📂 Project Overview

finTrack is a finance tracking app built with Django, designed to help users:

- Track income and expenses
- Manage financial goals
- Categorize transactions
- View summaries via an intuitive dashboard
- Export financial reports to Excel
- Register, log in, and manage accounts securely

---

## Project Structure

```
finTrack/
├── finance/                 # Main app for finance tracking
│   ├── models.py           # Transaction and Goal models
│   ├── views.py            # Class-based views for dashboard, transactions, goals
│   ├── forms.py            # Forms for registration, transactions, goals
│   ├── admin.py            # Admin interface with import/export
│   ├── templates/          # HTML templates
│   └── migrations/         # Database migrations
├── finTrack/               # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL routing
│   └── wsgi.py             # WSGI configuration
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## ⚙️ Quick Summary

- **Inputs:** Python 3.8+ and a virtual environment  
- **Outputs:** Running development server with a working finance tracking app  
- **Error Modes:** Missing dependencies, unapplied migrations, or database issues  
- **Success Indicator:** App runs locally using:  
  ```
  python manage.py runserver
  ```

---

## 🧩 Prerequisites

- Python 3.8+
- pip package manager
- (Optional) Git

If a requirements.txt file is missing, install Django manually and generate one using:
```
pip install django
pip freeze > requirements.txt
```

---

## 🚀 Setup Instructions (Windows PowerShell)

Run the following commands from the project root:

1. Create and activate a virtual environment
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies
```
if (Test-Path requirements.txt) { pip install -r requirements.txt } else { pip install django }
```

3. Apply migrations
```
python manage.py migrate
```

4. Create a superuser
```
python manage.py createsuperuser
```

5. Start the development server
```
python manage.py runserver
```

✅ Tip: After installing new dependencies, update your requirements.txt:
```
pip freeze > requirements.txt
```

---

## 🧪 Common Tasks

Run Tests:
```
python manage.py test
```

Collect Static Files (for production):
```
python manage.py collectstatic
```

---

## 🎨 Templates

- Templates are stored in:
```
finance/templates/finance/
``` 

- Base template:
```
base.html
```

Other templates extend base.html using Django’s {% extends %} syntax.

---

## 🌐 Deployment Notes

For production:

- Set in settings.py:
```
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']
```

- Use a production server like:

Gunicorn (WSGI)
Uvicorn (ASGI)

- Serve static files with Nginx/Apache
- Use HTTPS and environment variables
- Use PostgreSQL as the production database

---

## 🧭 Recommended Next Steps

- Add CONTRIBUTING.md
- Add GitHub Actions CI workflow
- Add open-source license (MIT, GPL, etc.)
- Add .env support using python-dotenv
- Extend features:
Budgeting tools
Chart-based analytics
API endpoints with Django REST Framework

---

Made with ❤️ using Django
