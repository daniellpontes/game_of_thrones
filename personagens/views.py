from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Personagens
from .forms import PersonagemForm


def lista_personagens(request):
    carac = Personagens.objects.values('id_personagem', 'nome', 'sobrenome', 'idade', 'apelido', 'especie')
    return render(request, 'lista_personagens.html', {'personagens': carac})


def cadastra_personagem(request):
    formulario = PersonagemForm(request.POST or None, request.FILES or None)
    # Se já algo no POST, o Django preenche o formulário. Se não, o formulário fica vazio.
    if formulario.is_valid():
        # Verifica se o formulário é válido e o salva, transformando-o em um objeto.
        formulario.save()
        messages.success(request, 'Personagem cadastrado com sucesso.')
        return redirect('lista_personagens_url')
    return render(request, 'cadastra_personagem.html', {'formulario': formulario})
    # Renderiza o template com o conteúdo da variável formulário
