from django.urls import path
from .views import lista_editoras, cadastra_editora, lista_autores, cadastra_autor


urlpatterns = [
    path('editoras/lista/', lista_editoras, name="lista_editoras_url"),
    path('editoras/cadastra/', cadastra_editora, name="cadastra_editora_url"),
    path('autores/lista/', lista_autores, name="lista_autores_url"),
    path('autores/cadastra', cadastra_autor, name="cadastra_autor_url")
]
