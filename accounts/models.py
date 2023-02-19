from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is_admin', default=False)
    is_employee = models.BooleanField('Is_employee', default=False)
    is_customer = models.BooleanField('Is_customer', default=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    dob = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed