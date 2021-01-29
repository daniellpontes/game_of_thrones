from django.forms import ModelForm
from .models import Editoras, Autores


class EditoraForm(ModelForm):
    class Meta:
        model = Editoras
        fields = ['editora', 'razao_social', 'pagina', 'ativo']


class AutorForm(ModelForm):
    class Meta:
        model = Autores
        fields = ['first_name', 'last_name', 'ano_nascimento', 'pais_nascimento', 'pagina', 'ativo']