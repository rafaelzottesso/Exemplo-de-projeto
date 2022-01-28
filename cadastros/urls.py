from django.urls import path

from .views import EstadoCreate, CidadeCreate
from .views import EstadoUpdate, CidadeUpdate
from .views import EstadoList, CidadeList

urlpatterns = [
    # Criar todos os endereços/rotas
    # path('endereço/', MinhaView.as_view(), name='referência/apelido'),

    path('inserir/estado/', EstadoCreate.as_view(), name='cadastrar-estado'),
    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name='editar-estado'),
    path('listar/estado/', EstadoList.as_view(), name='listar-estado'),

    path('inserir/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('listar/cidade/', CidadeList.as_view(), name='listar-cidade'),
    
]
