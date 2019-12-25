import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project_StarNavi.settings')

application = get_wsgi_application()
