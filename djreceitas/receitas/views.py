from django.shortcuts import redirect, render, get_object_or_404
from .models import Receita

def index(request) -> render:
    receitas = Receita.objects.all()
    
    return render(request, 'index.html', {
        'receitas': receitas
    })

def receita(request, receita_id: int) -> render:
    receita = Receita.objects.filter(id=receita_id)

    if not receita:
        return render(request, 'receita_nao_encontrada.html')

    return render(request, 'receita.html', {
        'receita': receita.get()
    })