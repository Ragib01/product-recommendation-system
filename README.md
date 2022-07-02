# product-recommendation-system: A Django project to show weather based product recommendation.
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)
## Database design:
![logs](https://github.com/Ragib01/product-recommendation-system/blob/main/database.PNG?raw=true)

Database configuration:
***core/settings.py*** file
```python
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': 'prs',  
        'USER': 'postgres',  
        'PASSWORD': '123',  
        'HOST': 'localhost'  
  }  
}
```

## Backend development workflow
```python
python -m venv venv
pip install requirements.txt
```
```python
python manage.py makemigrations
python manage.py migrate
```
Create superuser:
```python
python manage.py createsuperuser
```
Run the project:
```python
python manage.py runserver
