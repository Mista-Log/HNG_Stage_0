# Django Project

## Description

This is a Django project that serves as a starting point for building web applications. It includes a basic setup with Django, a powerful web framework that allows for rapid development and clean, pragmatic design.

## Features

- Admin interface for managing data
- RESTful API endpoints

## Requirements

- Python 3.x
- Django 3.x
- pip (Python package installer)

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone git@github.com:Mista-Log/HNG_Stage_0.git
    cd yourproject
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/`

## Project Structure

```
hng_stage_0/
├── baseapp/
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── env/
│   ├── include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
├── hng_stage_0/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── db.sqlite3
├── manage.py
├── Procfile
├── readme.md
├──requirements.txt
└── runtime.txt
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

