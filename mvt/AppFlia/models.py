from django.db import models

class Flia(models.Model):

    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    edad = models.IntegerField()
    
# Create your models here.
