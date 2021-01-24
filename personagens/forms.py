from django.forms import ModelForm
from .models import Personagens


class PersonagemForm(ModelForm):
    class Meta:
        model = Personagens
        fields = ['nome', 'sobrenome', 'idade', 'apelido', 'especie']