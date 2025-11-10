🐍 finTrack
A Django-based personal finance tracking application. Perfect for managing income, expenses, setting financial goals, and monitoring savings progress.

📂 Project Overview
A finance app for tracking transactions and goals
User authentication and registration
Dashboard with financial summaries and goal progress
Transaction management with categories
Excel export functionality for reports
Preconfigured settings for local development

Project Structure
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

⚙️ Quick Summary
Inputs: Python 3.8+ and a virtual environment
Outputs: Running development server with a working finance tracking app
Error Modes: Missing dependencies, unapplied migrations, or database issues
Success Indicator: The site runs locally when you execute python manage.py runserver

🧩 Prerequisites
Python 3.8+

pip package manager

(Optional) Git for version control

If a requirements.txt file is missing, install Django manually and generate one using:

pip install django
pip freeze > requirements.txt

🚀 Setup Instructions (Windows PowerShell)
Run the following commands from the project root:

Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

Install dependencies
if (Test-Path requirements.txt) { pip install -r requirements.txt } else { pip install django }

Apply migrations
python manage.py migrate

Create a superuser
python manage.py createsuperuser

Start the development server
python manage.py runserver

✅ Tip: After installing new dependencies, update your requirements.txt:

pip freeze > requirements.txt

🧪 Common Tasks
Run Tests:
python manage.py test

Collect Static Files (for production):
python manage.py collectstatic

🎨 Templates
Global templates: finance/templates/finance/
The base HTML layout is located at finance/templates/finance/base.html, extended by other pages like dashboard.html, transaction_form.html, etc.

🌐 Deployment Notes
For production deployment:

Set:
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

Use a proper WSGI/ASGI server (e.g., Gunicorn or Uvicorn)
Serve static files using Nginx, Apache, or a CDN
Secure the app with environment variables and HTTPS
Configure a production database (PostgreSQL recommended)

🧭 Recommended Next Steps
Add a requirements.txt with pinned versions (already present)
Create a CONTRIBUTING.md for collaboration guidelines
Add a CI workflow (e.g., GitHub Actions) to run tests automatically
Include a LICENSE file for open-source distribution
Configure .env files for secret management
Add more features like budgeting, charts, or API endpoints

Made with ❤️ using Django
