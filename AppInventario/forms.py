from django.forms import ModelForm, TextInput, Select, ModelMultipleChoiceField, CheckboxSelectMultiple, DateInput
from .models import TipoProducto, UnidadMedida, TipoEquipo, Marca, Equipo, Producto, OrdenIngreso, OrdenEgreso
from django import forms

class TipoProductoForm(ModelForm):
    class Meta:
        model = TipoProducto
        fields = ['nombre', 'unidad_medida']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control rounded-3'}),
            'unidad_medida': Select(attrs={'class': 'form-control rounded-3'}),
        }
    nombre = TextInput()
    unidad_medida = Select()

class UnidadMedidaForm(ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ["nombre","simbolo"]
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control rounded-3'}),
            'simbolo': TextInput(attrs={'class': 'form-control rounded-3'}),
        }

class TipoEquipoForm(ModelForm):
    class Meta:
        model = TipoEquipo
        fields = ["nombre", "tipo_producto"]
        widgets = {
            "nombre": TextInput(attrs={'class': 'form-control rounded-3'}),
            "tipo_producto": CheckboxSelectMultiple(attrs={'class':"form-check-input"})
        }
    
    nombre = TextInput()
    tipo_producto = ModelMultipleChoiceField(
        queryset=TipoProducto.objects.all(),
        widget=CheckboxSelectMultiple,
    )


class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ["nombre"]
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control rounded-3'})
        }
    nombre = TextInput()

class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'tipo_equipo', 'productos']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control rounded-3'}),
            'tipo_equipo': Select(attrs={'class': 'form-control rounded-3'}),

            'productos': CheckboxSelectMultiple(attrs={'class':"form-check-input"}),
        }
    nombre = TextInput()
    tipo_equipo = Select()
    productos = ModelMultipleChoiceField(
        queryset=Producto.objects.all(),
        widget=CheckboxSelectMultiple,
    )


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['tipo_producto', 'modelo', 'marca', 'numero_serie']
        widgets = {
            'tipo_producto': Select(attrs={'class': 'form-control rounded-3'}),
            'modelo': TextInput(attrs={'class': 'form-control rounded-3'}),
            'marca': Select(attrs={'class': 'form-control rounded-3'}),
            'numero_serie': TextInput(attrs={'class': 'form-control rounded-3'})
        }

ProductoFormSet = forms.modelformset_factory(Producto, form=ProductoForm, extra=1)

class OrdenIngresoForm(ModelForm):
    class Meta:
        model = OrdenIngreso
        fields = ['proveedor', 'fecha']
        widgets = {
            'proveedor': Select(attrs={'class': 'form-control rounded-3'}),
            'fecha': DateInput(attrs={'class': 'form-control rounded-3'})
        }


class OrdenEgresoForm(ModelForm):
    class Meta:
        model = OrdenEgreso
        fields = ['destino', 'fecha', 'comentario']
        widgets = {
            'destino': Select(attrs={'class': 'form-control rounded-3'}),
            'fecha': DateInput(attrs={'class': 'form-control rounded-3'}),
            'comentario': TextInput(attrs={'class': 'form-control rounded-3'}),
        }