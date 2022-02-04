from django.shortcuts import redirect, render, get_object_or_404
from .models import Receita


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
