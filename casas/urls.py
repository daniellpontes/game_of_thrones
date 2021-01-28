from django.urls import path
from .views import lista_casas, cadastra_casa, lista_membros, edita_casa, deleta_casa, cadastra_membro


urlpatterns = [
    path('cadastra/', cadastra_casa, name="cadastra_casa_url"),
    path('edita/<int:id_casa>', edita_casa, name="edita_casa_url"),
    path('lista/', lista_casas, name="lista_casas_url"),
    path('deleta/', deleta_casa, name="deleta_casa_url"),
    path('lista_membros/<int:id_casa>/', lista_membros, name="lista_membros_url"),
    path('cadastra_mebros/<int:id_casa>/', cadastra_membro, name="cadastra_membro_url")
]
