import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctor_booking_tool.settings')

application = get_asgi_application()
