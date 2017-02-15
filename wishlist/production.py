from .settings import *
import os

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(',')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
SECRET_KEY = os.environ.get("SECRET_KEY")
