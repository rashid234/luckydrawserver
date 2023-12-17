from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # Add your additional fields here
    roles = models.SmallIntegerField()
    phonenumber = models.CharField(max_length=10)