from django_backend.settings import *

DATABASE_PASSWORD = ''
EMAIL_HOST_PASSWORD = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}