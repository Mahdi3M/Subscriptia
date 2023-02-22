from django.db import models
from accounts.models import User

# Create your models here.

class QA(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    ques = models.TextField(max_length=500)
    ans = models.TextField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.ques