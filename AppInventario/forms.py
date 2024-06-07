from django.forms import ModelForm, TextInput
from .models import UnidadMedida

class UnidadMedidaForm(ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ["nombre","simbolo"]