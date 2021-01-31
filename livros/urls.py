from django.urls import path
from .views import editoras_lista, editora_cadastra, autores_lista, autor_cadastra, livros_lista, livro_cadastra, capitulos_lista, capitulo_cadastra


urlpatterns = [
    path('editoras/lista/', editoras_lista, name="lista_editoras_url"),
    path('editoras/cadastra/', editora_cadastra, name="cadastra_editora_url"),
    path('autores/lista/', autores_lista, name="lista_autores_url"),
    path('autores/cadastra', autor_cadastra, name="cadastra_autor_url"),
    path('livros/lista/', livros_lista, name="url_livros_lista"),
    path('livros/cadastra/', livro_cadastra, name="url_livro_cadastra"),
    path('capitulos/lista/<int:id_livro>/', capitulos_lista, name="url_capitulos_lista"),
    path('capitulos/cadastra/<int:id_livro>/', capitulo_cadastra, name="url_capitulo_cadastra")
]
