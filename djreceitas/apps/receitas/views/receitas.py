from pydoc import pager
from urllib.request import Request
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from receitas.models import Receita, Categoria
from django.contrib.auth.models import User
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from math import ceil


def index(request) -> render:
    receitas = Receita.objects.filter(publicar=True).order_by('-data_receita')
    
    receitas_por_pagina = Paginator(receitas, 5).get_page(
        request.GET.get('page')
    )

    return render(request, 'index.html', {
        'receitas': receitas_por_pagina
    })


def receita(request, receita_id: int) -> render:
    receitas = Receita.objects.filter(publicar=True)
    receita = Receita.objects.filter(id=receita_id, pessoa=request.user.id) if request.user.is_authenticated else receitas.filter(id=receita_id)
    categorias = [r.categoria for r in receitas.distinct('categoria')]

    if not receita:
        return render(request, 'receita_nao_encontrada.html')


    return render(request, 'receita.html', {
        'receita': receita.get(), 'categorias': categorias + [receita.get().categoria]
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

            messages.success(request, f'Receita \"{request.POST.get("nome_receita")}\" criada com sucesso!')
            
            return redirect('receitas_criar')

        return render(request, 'criar_receita.html')
    else:
        return redirect('usuarios_login')

def deletar(request, receita_id) -> redirect:
    if request.user.is_authenticated:
        receita = Receita.objects.filter(pessoa=request.user.id, id=receita_id)
        if receita.exists():
            messages.success(request, f'\"{receita.get().nome}\" foi deletado com sucesso')
            receita.delete()
        return redirect('usuarios_dashboard')

    return redirect('receitas_index')

def publicar(request, receita_id) -> redirect:
    if request.user.is_authenticated:
        receita = Receita.objects.filter(pessoa=request.user.id, id=receita_id)
        if receita.exists():
            receita = receita.get()

            messages.success(request, f'"{receita.nome}" foi {"Privado" if receita.publicar else "Publicado"}')
            receita.publicar = not receita.publicar
            receita.save()
                
        return redirect('usuarios_dashboard')

    return redirect('receitas_index')

def editar(request: Request, receita_id: int) -> render:
    receita = Receita.objects.get(id=receita_id, pessoa=request.user.id)
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        receita.nome = request.POST.get('nome_receita')
        receita.ingredientes = request.POST.get('ingredientes')
        receita.modo_preparo = request.POST.get('modo_preparo')
        receita.tempo_preparo = request.POST.get('tempo_preparo')
        receita.rendimento = request.POST.get('rendimento')

        if receita.categoria.nome != request.POST.get('categoria'):
            categoria = Categoria.objects.filter(nome=request.POST.get('categoria'))
            receita.categoria = categoria if categoria.exists() else categoria.create(nome=request.POST.get('categoria'))
        
        if 'foto_receita' in request.FILES:
            receita.foto_receita = request.FILES.get('foto_receita')
        
        receita.save()
        messages.success(request, 'Receita atualizada com sucesso!')


    return render(request, 'editar_receita.html', {
        'receita': receita, 'categorias': categorias
    })
