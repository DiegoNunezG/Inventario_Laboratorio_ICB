# forms.py
from django import forms
from .models import Medida

class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = Medida
        widgets = {
            'unidad_de_medida': forms.Select(attrs={'class': 'form-control rounded-3'})
        }
