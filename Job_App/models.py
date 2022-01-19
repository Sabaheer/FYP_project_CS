from email.mime import image
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    Email = models.EmailField(max_length=20)
    type = models.CharField(max_length=15, null=True)

    def _str_(self):
        return self.user.username
