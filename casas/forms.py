from django.forms import ModelForm
from .models import Casas


class CasaForm(ModelForm):
    class Meta:
        model = Casas
        fields = ['nome_casa', 'lema', 'simbolo']
