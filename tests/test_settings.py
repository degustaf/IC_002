""" Module to contain testing settings."""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "WordMadness",
    "tests",
    ]
ROOT_URLCONF = 'WordMadness.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
