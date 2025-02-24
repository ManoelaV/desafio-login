from django.urls import path
from .views import register_view, login_view, menu_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('menu/', menu_view, name='menu'),
    
]