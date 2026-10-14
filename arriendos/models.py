from django.db import models

# Create your models here.
class Equipo(models.Model):

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    valor = models.PositiveIntegerField()
    arrendado = models.BooleanField()
    fecha_ingresado = models.DateField()
    fecha_arrendado = models.DateField()

    def __str__(self) -> str:
        return self.nombre
    
class Arriendo(models.Model):

    cliente = models.CharField(max_length=150, unique=True)
    garantia = models.BooleanField()
    total_pagado = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.cliente