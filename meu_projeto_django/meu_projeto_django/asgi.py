import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_projeto_django.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # (http->django views is added by default)
})