from django.urls import path
from .views import lista_personagens, cadastra_personagem


urlpatterns = [
    path('lista/', lista_personagens, name="lista_personagens_url"),
    path('cadastra/', cadastra_personagem, name="cadastra_personagem_url")
]
