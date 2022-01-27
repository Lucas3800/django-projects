from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='receitas_index'),
    path('receita/', views.receita, name='receitas_receita'),
]