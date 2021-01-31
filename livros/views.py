from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Editoras, Autores, Livros, Capitulos
from .forms import EditoraForm, AutorForm, LivroForm, CapituloForm


@login_required
def editoras_lista(request):
    editoras = Editoras.objects.all()
    return render(request, 'editoras_lista.html', {'editoras': editoras})


@login_required
def editora_cadastra(request):
    formulario = EditoraForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Editora cadastrada com sucesso.')
        return redirect('lista_editoras_url')
    return render(request, 'editoras_cadastra.html', {'formulario': formulario})


@login_required
def autores_lista(request):
    autores = Autores.objects.all()
    return render(request, 'autores_lista.html', {'autores': autores})


@login_required
def autor_cadastra(request):
    formulario = AutorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Autor cadastrado com sucesso.')
        return redirect('lista_autores_url')
    return render(request, 'autores_cadastra.html', {'formulario': formulario})


@login_required
def livros_lista(request):
    livros = Livros.objects.all()
    return render(request,'livros_lista.html', {'livros': livros})


@login_required
def livro_cadastra(request):
    formulario = LivroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Livro cadastrado com sucesso.')
        return redirect('url_livros_lista')
    return render(request, 'livros_cadastra.html', {'formulario': formulario})


@login_required
def capitulos_lista(request, id_livro):
    capitulos = Capitulos.objects.all()
    capitulos = {'capitulos': capitulos.filter(id_livro=id_livro), 'livro': Livros.objects.get(pk=id_livro)}
    return render(request, 'capitulos_lista.html', capitulos)


@login_required
def capitulo_cadastra(request, id_livro):
    formulario = CapituloForm(request.POST or None, request.FILES or None)
    livro = Livros.objects.get(pk=id_livro)
    if formulario.is_valid():
        instance = formulario.save(commit=False)
        instance.id_llivro = livro
        instance.save()
        messages.success(request, 'Capítulo cadastrado com sucesso.')
        return redirect('url_capitulos_lista', id_livro=id_livro)
    return render (request, 'capitulos_cadastra.html', {'formulario': formulario, 'livro': livro})
