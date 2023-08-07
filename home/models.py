from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    write = models.TextField()

class Registration(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    repeat = models.CharField(max_length=30)
