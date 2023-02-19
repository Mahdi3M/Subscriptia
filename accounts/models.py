from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is_admin', default=False)
    is_employee = models.BooleanField('Is_employee', default=False)
    is_customer = models.BooleanField('Is_customer', default=True)