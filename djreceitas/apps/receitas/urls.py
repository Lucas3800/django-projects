from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='receitas_index'),
    path('receita/<int:receita_id>', receita, name='receitas_receita'),
    path('buscar', buscar, name='receitas_buscar'),
    path('criar/', criar_receita, name='receitas_criar'),
    path('deletar/<int:receita_id>', deletar, name='receitas_deletar'),
    path('publicar/<int:receita_id>', publicar, name='receitas_publicar'),
    path('editar/<int:receita_id>', editar, name='receitas_editar'),
]