from django.forms import ModelForm, TextInput, Select, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import TipoProducto, UnidadMedida, TipoEquipo

class TipoProductoForm(ModelForm):
    class Meta:
        model = TipoProducto
        fields = ['nombre', 'unidad_medida']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control rounded-3'}),
            'unidad_medida': Select(attrs={'class': 'form-control rounded-3'}),
        }

class UnidadMedidaForm(ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ["nombre","simbolo"]

class TipoEquipoForm(ModelForm):
    class Meta:
        model = TipoEquipo
        fields = ["nombre", "tipo_producto"]
    
    nombre = TextInput()
    tipo_producto = ModelMultipleChoiceField(
        queryset=TipoProducto.objects.all(),
        widget=CheckboxSelectMultiple,
    )

