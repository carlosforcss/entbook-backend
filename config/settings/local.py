from .base import *

SECRET_KEY = 'c@4&!wy@@(m43-5@uo_&ablg%&tr9ve#!l2n0tyvv%$*c9(mhr'
ALLOWED_HOSTS = ["*"]
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
