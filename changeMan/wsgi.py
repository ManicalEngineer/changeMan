"""
WSGI config for changeMan project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application


sys.path.append('/var/www/changeMan')
sys.path.append('/var/www/changeMan/changeMan')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'changeMan.settings')

application = get_wsgi_application()

