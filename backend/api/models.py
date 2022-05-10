from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    github = models.CharField(max_length=80, blank=True, null=True)
    linkedin = models.CharField(max_length=80, blank=True, null=True)
    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password']
