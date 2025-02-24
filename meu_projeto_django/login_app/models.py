from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Garante que o e-mail seja único

    def __str__(self):
        return self.email