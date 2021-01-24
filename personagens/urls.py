from django.urls import path
from .views import lista_personagens


urlpatterns = [
    path('lista/', lista_personagens, name="lista_personagens")
]
