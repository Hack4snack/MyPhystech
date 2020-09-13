"""
WSGI config for MyPhystech project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import sys

from .settings import BASE_DIR

# assuming your Django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = BASE_DIR
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyPhystech.settings')

application = get_wsgi_application()
