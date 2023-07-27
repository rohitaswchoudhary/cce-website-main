import os
import sys
path = '/home/rohitaswchoudhary/cce-website-main'
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'cce.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()