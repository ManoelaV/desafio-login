from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Registre o modelo User personalizado
admin.site.register(CustomUser, UserAdmin)