from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from receitas.models import Receita
from django.contrib import messages

from datetime import datetime


def cadastro(request) -> render:
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        criar_novo_cadastro = True

        if password != password2:
            messages.error(request, 'As senhas não são correspondentes')
            criar_novo_cadastro = False


        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado em nossa base de dados')
            criar_novo_cadastro = False

        if criar_novo_cadastro:
            User.objects.create_user(username=nome, email=email, password=password).save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('usuarios_login')

    return render(request, 'usuarios/cadastro.html')

def login(request) -> render:
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = User.objects.filter(email=email).values_list('username', flat=True)

        if username.exists():
            user = auth.authenticate(username=username.get(), password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('usuarios_dashboard')

        messages.error(request, 'E-mail ou senha incorretas')
        return redirect('usuarios_login')


    return render(request, 'usuarios/login.html')

def dashboard(request) -> render:
    if request.user.is_authenticated:
        receitas = Receita.objects.filter(pessoa=request.user.id).order_by('-data_receita')

        return render(request, 'usuarios/dashboard.html', {
            'receitas': receitas   
        })
    else:
        return redirect('usuarios_login')

def logout(request) -> render:
    auth.logout(request)

    return redirect('receitas_index')
