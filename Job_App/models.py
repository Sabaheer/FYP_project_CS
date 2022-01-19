from email.mime import image
from operator import mod
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=15, null=True)

    def _str_(self):
        return self.user.username
