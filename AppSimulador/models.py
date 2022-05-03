from django.db import models
from django.forms import CharField

class Vendedor(models.Model):

   
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    legajo = models.IntegerField()
    
    def __str__(self):
        return f"Nombre del vendedor: {self.nombre} {self.apellido}, legajo: {self.legajo}."

class Cliente(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    tipoFacturacion = models.CharField(max_length=100) 
    
        
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, dni : {self.dni} con factura {self.tipoFacturacion}."

class Producto(models.Model):

    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()   
    stock = models.IntegerField() 

    def __str__(self):
        return f"Producto {self.nombre}, precio {self.precio} $, stock {self.stock}."  