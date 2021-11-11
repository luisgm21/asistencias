from typing import Tuple
from django.db import models


   

class Persona(models.Model):
    GENERO_OPCIONES = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    )
    dni = models.CharField(max_length=8, unique=True)
    nombre_completo = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=9, choices=GENERO_OPCIONES)
    domicilio = models.CharField(max_length=250)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nombre_completo',)

    def __str__(self):
        return '{}'.format(self.nombre_completo)


class EstadoSalud(models.Model):
    
    es_discapacitado = models.BooleanField(null=True)
    posee_obesidad = models.BooleanField(null=True)
    posee_desnutricion = models.BooleanField(null=True)
    observaciones = models.TextField(blank=True)

#Definimos el modelo Cuenta
class CuentaBancaria(models.Model):
   #Definimos la tupla con las opciones de banco
   OPCIONES_BANCO = (
       ('nacion','Nacion'),
       ('santader','Santander'),
       ('galicia','Galicia')
   )
   
   numero_cuenta = models.IntegerField(unique=True)
   cbu = models.IntegerField()
   alias = models.CharField(max_length=100,unique=True)
   banco_emisor = models.CharField(max_length=100,choices=OPCIONES_BANCO)
   persona = models.OneToOneField(Persona, on_delete=models.CASCADE,null=True,blank=True)
   
   #Hacemos que muestre el cbu en lugar de la referencia
   def __str__(self):
        return f"CBU:{self.cbu}"
