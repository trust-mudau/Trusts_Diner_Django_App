# Trust's Diner

A responsive Django restaurant menu with an admin-managed catalogue, list and detail pages, secure environment-based settings, and automated view tests.

## Features

- Alphabetically ordered menu cards with prices and descriptions
- Accessible item detail pages and shared responsive layout
- Django admin search and list display for menu items
- Initial database migration included
- Production settings controlled through environment variables
- Tests for list, detail, missing-item, and model behavior

## Run locally

```bash
cd Trusts_Diner_Django_App
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the menu and `/admin/` to manage items.

## Configuration

Copy `.env.example` values into your deployment environment. When `DJANGO_DEBUG=false`, `DJANGO_SECRET_KEY` is required. Set `DJANGO_ALLOWED_HOSTS` and `DJANGO_CSRF_TRUSTED_ORIGINS` to the exact deployed domains.

## Verification

```bash
python manage.py check
python manage.py test
python manage.py makemigrations --check
```
