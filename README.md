# Restaurant Menu Website

## Overview
This is a Django-based web application for viewing and interacting with a restaurant menu. It displays meal categories, descriptions, prices, and images for each item, and includes an admin panel for menu management.

## Features
- Categorized display of restaurant meals (starters, salads, main dishes, desserts)
- Interactive menu with prices, availability status, and meal descriptions
- Admin panel for menu item management
- Responsive design using Bootstrap

## Requirements
- Python 3.x
- Django 3.x or later
- Pillow (for image handling)
- Bootstrap 5 (via CDN)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/restaurant-menu.git
cd restaurant-menu
```

### 2. Set Up Virtual Environment
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
# Or manually:
pip install django pillow
```

### 4. Configure Database
Default: SQLite. For other databases, update `DATABASES` in `settings.py`.

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```
Access at: http://127.0.0.1:8000/

## Media Setup
Configure in `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Update `urls.py`:
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Your URL patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Admin Panel
Access at: http://127.0.0.1:8000/admin/

## File Structure
```
restaurant-menu/
├── restaurant_menu/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── models.py
├── templates/
│   ├── base.html
│   ├── index.html
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

## Adding Meals
1. Access Admin panel
2. Add new meals with:
   - Name
   - Description
   - Price
   - Meal type
   - Status
   - Image (optional)

