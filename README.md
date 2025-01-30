# yk-belgium
- Create virtual python environment : 
    python -m venv .venv

- Install django : 
    python pip install django

- Activate virtual environment : 
    .\venv\Scripts\activate

- Create django project :
    django-admin startproject realtor_client

- Create django application : 
    python manage.py startapp appartements
    python manage.py startapp odoo_config

- Run django website : python manage.py runserver

- Create super-user to acces to admin database site : python manage.py createsuperuser

- Run migration : 
    python manage.py makemigrations
    python manage.py migrate

- Install crispy : 
    pip install django-crispy-forms
    pip install crispy-bootstrap5

- Install dotenv to set venv in os :
    pip install python-dotenv

- Load environnement variable :
    from dotenv import load_dotenv
    load_dotenv()

- Acces to venv : 
    import os
    SECRET_KEY = os.getenv('VARIABLE_NAME')
