from django.forms import ModelForm
from .models import Editoras, Autores, Livros, Capitulos


class EditoraForm(ModelForm):
    class Meta:
        model = Editoras
        fields = ['editora', 'razao_social', 'pagina', 'ativo']


class AutorForm(ModelForm):
    class Meta:
        model = Autores
        fields = ['first_name', 'last_name', 'ano_nascimento', 'pais_nascimento', 'pagina', 'ativo']


class LivroForm(ModelForm):
    class Meta:
        model = Livros
        fields = ['id_editora', 'id_autor', 'titulo', 'isbn', 'edicao_numero', 'edicao_ano', 'num_paginas']


class CapituloForm(ModelForm):
    class Meta:
        model = Capitulos
        exclude = ['id_capitulo']
