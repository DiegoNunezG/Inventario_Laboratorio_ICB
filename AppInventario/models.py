from django.db import models
from django.core.validators import MinValueValidator, StepValueValidator

# Create your models here.
class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    simbolo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class TipoEquipo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    tipo_producto = models.ManyToManyField(TipoProducto)

    def __str__(self):
        return self.nombre
    

class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=150)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    numero_serie = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.modelo


class Equipo(models.Model):
    nombre = models.CharField(max_length=100, unique=True, default='')
    tipo_equipo = models.ForeignKey(TipoEquipo, on_delete=models.PROTECT)
    productos = models.ManyToManyField(Producto, blank=True)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    rut = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    

class OrdenIngreso(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    fecha = models.DateField()

class OrdenEgreso(models.Model):
    destino = models.CharField(max_length=100)
    fecha = models.DateField()
    comentario = models.CharField(max_length=250)

class DetalleIngreso(models.Model):
    orden = models.ForeignKey(OrdenIngreso, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1, blank=False, validators=[MinValueValidator(1), StepValueValidator(1)])


class DetalleEgreso(models.Model):
    orden = models.ForeignKey(OrdenEgreso, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
