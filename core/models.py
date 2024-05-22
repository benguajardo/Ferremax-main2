from datetime import timezone
from django.conf import settings
from django.db import models
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render, redirect



class Region(models.Model):
    descripcion = models.CharField(max_length=50)
    def  __str__(self):
        return self.descripcion

class Comuna(models.Model):
    descripcion = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    numero = models.IntegerField()
    def  __str__(self):
        return self.descripcion

class Direccion(models.Model):
    descripcion = models.CharField(max_length=50)
    def  __str__(self):
        return self.descripcion



class TipoEmpleado(models.Model):
    descripcion = models.CharField(max_length=50)
    def  __str__(self):
        return self.descripcion

class TipoProducto(models.Model):
    descripcion = models.CharField(max_length=50)
    def  __str__(self):
        return self.descripcion

class Marca(models.Model):
    descripcion = models.CharField(max_length=50)
    def  __str__(self):
        return self.descripcion

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    telefono = models.IntegerField
    fechaNac = models.DateField
    def  __str__(self):
        return self.nombre+self.apellido

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sueldo = models.IntegerField
    fechaNac = models.DateField
    tipo = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    def  __str__(self):
        return self.nombre+self.apellido
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.CharField(max_length=50)
    tipo_id = models.IntegerField()
    marca_id = models.IntegerField()
    stock = models.IntegerField()
    def  __str__(self):
        return self.nombre
    
class Boleta(models.Model):
    fecha = models.DateField
    total = models.IntegerField
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def  __str__(self):
        return self
    
class DetalleBol(models.Model):
    cantidad = models.PositiveIntegerField(default=1)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    def  __str__(self):
        return self.producto.nombre+' x'+self.cantidad

class Envio(models.Model):
    descripcion = models.CharField(max_length=50)
    total = models.IntegerField
    fecha = models.DateField
    destino = models.CharField(max_length=50)
    def  __str__(self):
        return self.descripcion
    
