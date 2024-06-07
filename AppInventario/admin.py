from django.contrib import admin
from .models import UnidadMedida, TipoProducto, TipoEquipo, Equipo, Marca, Producto, Proveedor, OrdenIngreso, OrdenEgreso

# Register your models here.
admin.site.register(UnidadMedida)
admin.site.register(TipoProducto)
admin.site.register(TipoEquipo)
#admin.site.register(ComponentesTipoEquipo)
admin.site.register(Equipo)
admin.site.register(Marca)
admin.site.register(Producto)
#admin.site.register(ComponentesEquipo)
admin.site.register(Proveedor)
admin.site.register(OrdenIngreso)
admin.site.register(OrdenEgreso)