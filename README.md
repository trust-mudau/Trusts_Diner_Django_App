# 🍽️ Trust's Diner Django App

A simple, responsive Django web app for a restaurant menu — built for **Trust's Diner** using **Django** and **Bootstrap 5**.

---

## 📖 Overview

**Trust’s Diner** is a minimal Django project designed to demonstrate the basics of:
- Building a Django app (`menu`)
- Displaying data from a model
- Using templates with Bootstrap for styling
- Navigating between list and detail views
- Organizing a clean project structure

The app allows visitors to:
- View all menu items in alphabetical order
- See each item’s name and price on the homepage
- Click on a menu item to view more details (name, price, description)
- Enjoy a consistent header, navigation, and footer across all pages

---

## 🧱 Project Structure

restaurant_site/
│
├── restaurant_site/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── menu/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── admin.py
│ └── templates/
│ └── menu/
│ ├── home.html
│ └── item_detail.html
│
└── manage.py

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1. Clone or Extract the Project

If you downloaded a ZIP:
```bash
unzip Trusts_Diner_Django_App.zip
cd restaurant_site_diner
If using Git:

bash
Copy code
git clone <repo_url>
cd restaurant_site_diner
2. Create a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
3. Install Django
bash
Copy code
pip install django
4. Apply Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
5. Create a Superuser (optional)
To access the Django admin panel:

bash
Copy code
python manage.py createsuperuser
Then log in at:
➡️ http://127.0.0.1:8000/admin/

6. Run the Development Server
bash
Copy code
python manage.py runserver
Then visit:
➡️ http://127.0.0.1:8000/

🖥️ Usage
The Home Page (/) lists all menu items in alphabetical order, showing:

Item name

Price

“View Details” button linking to the item’s page

The Item Detail Page (/item/<id>/) shows:

Item name

Price

Description

Each page includes:

A header with “Trust’s Diner” title and a navigation link to Home

A footer with © 2025 Trust’s Diner notice

🧩 Features
✅ Django-powered backend
✅ SQLite3 database
✅ Model for Menu Items
✅ Bootstrap 5 responsive styling
✅ Simple, clean UI
✅ Admin interface for managing items

📦 Model Structure
MenuItem model

Field	Type	Description
name	CharField	Name of the menu item
description	TextField	Description of the menu item
price	DecimalField	Price in Rands (R)

Menu items are automatically sorted alphabetically.

🎨 Styling
This app uses Bootstrap 5 for layout and components.
Styling includes:

Responsive card grid for menu items

Consistent header and footer

Clean, modern color scheme (dark header/footer, light background)

🧰 Tech Stack
Python 3

Django 5+

Bootstrap 5

SQLite3 (default Django database)

🧑‍💻 Developer Notes
You can add menu items via Django Admin.

To change footer text or branding, edit the templates:

menu/templates/menu/home.html

menu/templates/menu/item_detail.html

📜 License
This project is open for educational and personal use.
