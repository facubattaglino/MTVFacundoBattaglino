from django.db import models
# Create your models here.

class familia(models.Model):
    nombre = models.CharField(max_length= 30)
    apellido = models.CharField(max_length= 30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length= 50, blank= True, null= True)
