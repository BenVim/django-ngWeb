from django.db import models

# Create your models here.

class Memeber(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    addTime = models.IntegerField()
    token = models.CharField(max_length=200)



