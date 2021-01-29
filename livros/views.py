from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Editoras, Autores
from .forms import EditoraForm, AutorForm


def lista_editoras(request):
    editoras = Editoras.objects.all()
    return render(request, 'lista_editoras.html', {'editoras': editoras})


def cadastra_editora(request):
    formulario = EditoraForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Editora cadastrada com sucesso.')
        return redirect('lista_editoras_url')
    return render(request, 'cadastra_editora.html', {'formulario': formulario})


def lista_autores(request):
    autores = Autores.objects.all()
    return render(request, 'lista_autores.html', {'autores': autores})


def cadastra_autor(request):
    formulario = AutorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Autor cadastrado com sucesso.')
        return redirect('lista_autores_url')
    return render(request, 'cadastra_autor.html', {'formulario': formulario})
