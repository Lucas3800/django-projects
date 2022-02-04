from django.urls import path
from . import views


urlpatterns = [
    path('cadastro', views.cadastro, name='usuarios_cadastro'),
    path('login', views.login, name='usuarios_login'),
    path('dashboard', views.dashboard, name='usuarios_dashboard'),
    path('logout', views.logout, name='usuarios_logout'),
]

