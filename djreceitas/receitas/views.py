from django.shortcuts import redirect, render, get_object_or_404
from .models import Receita, Categoria
from django.contrib.auth.models import User
from datetime import datetime


def index(request) -> render:
    receitas = Receita.objects.filter(publicar=True).order_by('-data_receita')
        
    return render(request, 'index.html', {
        'receitas': receitas
    })


def receita(request, receita_id: int) -> render:
    receitas = Receita.objects.filter(publicar=True)
    receita = receitas.filter(id=receita_id)
    categorias = [r.categoria for r in receitas.distinct('categoria')]

    if not receita:
        return render(request, 'receita_nao_encontrada.html')


    return render(request, 'receita.html', {
        'receita': receita.get(), 'categorias': categorias
    })


def buscar(request):
    receitas = Receita.objects.filter(publicar=True).order_by('-data_receita')
    if 'q' in request.GET:
        termo_busca = request.GET.get('q')
        receitas = receitas.filter(nome__icontains=termo_busca)
    if 'categoria' in request.GET:
        categoria = request.GET.get('categoria')
        receitas = receitas.filter(categoria=categoria)
        
    return render(request, 'index.html', {
        'receitas': receitas
    })

def criar_receita(request) -> render:
    if request.user.is_authenticated:

        if request.method == 'POST':

            categoria = Categoria.objects.create(nome=request.POST.get('categoria'))
            user = User.objects.get(id=request.user.id)
            
            Receita.objects.create(
                nome = request.POST.get('nome_receita'),
                ingredientes = request.POST.get('ingredientes'),
                modo_preparo = request.POST.get('modo_preparo'),
                tempo_preparo = request.POST.get('tempo_preparo'),
                rendimento = request.POST.get('rendimento'),
                categoria = categoria,
                foto_receita = request.FILES.get('foto_receita'),
                pessoa = user
            ).save()

            redirect('usuarios_dashboard')

        return render(request, 'criar_receita.html')
    else:
        return redirect('usuarios_login')