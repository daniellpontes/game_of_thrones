from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Casas, Membros
from .forms import CasaForm


@login_required
def lista_casas(request):
    maisons = Casas.objects.values('id_casa', 'nome_casa', 'lema', 'simbolo').order_by('nome_casa')
    return render(request, 'lista_casas.html', {'houses': maisons})


@login_required
def lista_membros(request, id_casa):
    carac = Membros.objects.values('id_membro', 'id_personagem', 'id_personagem__nome',
                                   'id_personagem__sobrenome', 'id_personagem__apelido')
    membros = {'membros': carac.filter(id_casa=id_casa), 'casa': Casas.objects.get(pk=id_casa)}
    return render(request, 'lista_membros.html', membros)


@login_required
def cadastra_casa(request):
    formulario = CasaForm(request.POST or None, request.FILES or None)
    # Se já algo no POST, o Django preenche o formulário. Se não, o formulário fica vazio.
    if formulario.is_valid():
        # Verifica se o formulário é válido e o salva, transformando-o em um objeto.
        formulario.save()
        messages.success(request, 'Casa cadastrada com suncesso.')
        return redirect('lista_casas_url')
    return render(request, 'cadastra_casa.html', {'formulario': formulario})
    # Renderiza o template com o conteúdo da variável formulário


@login_required
def edita_casa(request, id_casa):
    casa = get_object_or_404(Casas, pk=id_casa)
    form = CasaForm(request.POST or None, request.FILES or None, instance=casa)
    if form.is_valid():
        form.save()
        return redirect('lista_casas_url')
    return render(request, 'edita_casa.html', {'formulario': form})


@login_required
def deleta_casa(request):
    if request.method == 'POST':
        id_casa = request.POST.get("id_casa")
        casa = get_object_or_404(Casas, pk=id_casa)
        membros = Membros.objects.filter(id_casa=casa)
        if membros:
            messages.error(request, 'Não é possível remover a casa ' + casa.nome_casa + ', pois ela possui membros.')
        else:
            casa.delete()
            messages.success(request, 'Casa removida com suncesso.')
            return redirect('lista_casas_url')
    return redirect('lista_casas_url')