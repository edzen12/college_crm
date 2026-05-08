from django.contrib.auth.models import AbstractUser
from django.db import models

# Преподаватели буду логиниться
# админы буду логиниться
# кураторы буду логиниться

class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        TEACHER = 'teacher', 'Teacher'
        CURATOR = 'curator', 'Curator'
    
    role = models.CharField(
        max_length=20,
        choices=Role.choices
    )