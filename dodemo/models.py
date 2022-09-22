from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DodemoModel(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

class Good(models.Model):
    author = 
