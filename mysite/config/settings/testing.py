from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']
SECRET_KEY = 'django-insecure-e2zj!rh5nmim3dvy($x@ks#9pa&e8+usyfedyqx87s-6sla+0r'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_testing.sqlite3'
    }
}
