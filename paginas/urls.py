from os import name
from django.urls import path
from .views import PaginaInicial, Sobre

urlpatterns = [
    # Criar todos os endereços/rotas
    # path('endereço/', MinhaView.as_view(), name='referência/apelido'),
    path('home/', PaginaInicial.as_view(), name='index'),
    path('', PaginaInicial.as_view(), name='index-2'),

    path('sobre/', Sobre.as_view(), name='sobre'),
    
]
