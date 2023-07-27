"""
WSGI config for cce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application
# from whitenoise import WhiteNoise

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cce.settings')


# application = get_wsgi_application()
# application = WhiteNoise(application,root="static")

import os

import sys
path = '/home/rohitaswchoudhary/cce-website-main'
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'CCE.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

app = application