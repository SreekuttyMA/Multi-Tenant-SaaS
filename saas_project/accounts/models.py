from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Organization(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class User(AbstractUser):
    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("USER", "User"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)