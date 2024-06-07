from django.db import models

# Create your models here.
class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=100)
    simbolo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class TipoProducto(models.Model):
    nombre = models.CharField(max_length=100)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class TipoEquipo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class ComponentesTipoEquipo(models.Model):
    tipo_equipo = models.ForeignKey(TipoEquipo, on_delete=models.PROTECT)
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.PROTECT)


class Equipo(models.Model):
    tipo_equipo = models.ForeignKey(TipoEquipo, on_delete=models.PROTECT)


class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=150)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    numero_serie = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.modelo


class ComponentesEquipo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class OrdenIngreso(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    fecha = models.DateField(auto_now_add=True)

class OrdenEgreso(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    comentario = models.CharField(max_length=250)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField(auto_now_add=True)
    destino = models.CharField(max_length=100)