from django.db import models

# Create your models here.

class CrearAlumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    curso = models.IntegerField()
    division = models.CharField(max_length=1)