from django.shortcuts import render


def cadastro(request) -> render:
    return render(request, 'usuarios/cadastro.html')

def login(request) -> render:
    return render(request, 'usuarios/login.html')

def dashboard(request) -> render:
    pass

def logout(request) -> render:
    pass
