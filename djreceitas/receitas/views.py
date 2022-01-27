from unicodedata import name
from django.shortcuts import render


def index(request) -> render:
    return render(request, 'index.html')

def receita(request) -> render:
    return render(request, 'receita.html')