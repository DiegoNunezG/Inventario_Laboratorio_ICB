from django.db import models

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
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    fecha = models.DateField()

class OrdenEgreso(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    comentario = models.CharField(max_length=250)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField()
    destino = models.CharField(max_length=100)