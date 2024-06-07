from django import forms
from .models import TipoProducto, UnidadMedida

class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = ['nombre', 'unidad_medida']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'unidad_medida': forms.Select(attrs={'class': 'form-control rounded-3'}),
        }