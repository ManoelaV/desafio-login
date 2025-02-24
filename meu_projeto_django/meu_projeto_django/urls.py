from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='login/')),  # Redireciona a URL raiz para /login/
    path('', include('login_app.urls')),  # Inclua as URLs do login_app
]