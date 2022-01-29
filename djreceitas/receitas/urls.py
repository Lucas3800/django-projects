from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='receitas_index'),
    path('receita/<int:receita_id>', views.receita, name='receitas_receita'),
]