from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class tablaregistros(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    
    create_user= models.DateTimeField (auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
       return self.nombre

class tablaaulas(models.Model):
    nombre= models.OneToOneField(tablaregistros, on_delete= models.CASCADE)
    aula= models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
       return self.aula