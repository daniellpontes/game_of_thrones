from django.forms import ModelForm, HiddenInput
from .models import Casas
from .models import Membros


class CasaForm(ModelForm):
    class Meta:
        model = Casas
        fields = ['nome_casa', 'lema', 'simbolo']


class MembroCasaForm(ModelForm):
    class Meta:
        model = Membros
        fields = ['id_casa', 'id_personagem', 'papel_casa']
        widgets = {'id_casa': HiddenInput()}