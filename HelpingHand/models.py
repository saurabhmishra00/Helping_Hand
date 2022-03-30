from pickle import TRUE
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,primary_key=True)
    password=models.CharField(max_length=50)

class Login(models.Model):
    email=models