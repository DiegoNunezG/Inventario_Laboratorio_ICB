from django.forms import ModelForm, TextInput, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import TipoEquipo, TipoProducto

class TipoEquipoForm(ModelForm):
    class Meta:
        model = TipoEquipo
        fields = ["nombre", "tipo_producto"]
    
    nombre = TextInput()
    tipo_producto = ModelMultipleChoiceField(
        queryset=TipoProducto.objects.all(),
        widget=CheckboxSelectMultiple,
    )