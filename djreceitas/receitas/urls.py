from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='receitas_index'),
    path('receita/<int:receita_id>', views.receita, name='receitas_receita'),
    path('buscar', views.buscar, name='receitas_buscar'),
    path('criar/', views.criar_receita, name='receitas_criar'),
]