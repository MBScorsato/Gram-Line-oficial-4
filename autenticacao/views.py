from django.contrib import messages, auth
from django.contrib.messages import constants
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/index/plataforma')
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # VERIFICA SE A SENHA E A CONFIRMAÇÃO SÃO IGUAIS
        if confirmar_senha != senha:
            messages.add_message(request, constants.ERROR, 'As senhas tem que ser iguais')
            return redirect('/auth/cadastro')

        # VERIFIQUE SE O FORMULÁRIO ESTA PREENCHIDO .STRIP NÃO CONSIDERA OS ESPAÇOS
        if len(username.strip()) < 0 or len(email.strip()) == 0 or len(senha.strip()) ==  0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/cadastro')

        # VERIFICA E INFORMA QUE SENHA QUE TER NO MÍNIMO 6 DIGITOS
        if len(senha.strip()) < 6:
            messages.add_message(request, constants.ERROR, 'A senha tem que ter pelo menos 6 digitos')
            return redirect('/auth/cadastro')

        user = User.objects.filter(username=username)
        user_email = User.objects.filter(email=email)
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse "nome" cadastrado')
            return redirect('/auth/cadastro')
        if user_email.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse "email" cadastrado')
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=senha)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso')
            return redirect('/auth/logar')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/auth/cadastro')


def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/index/plataforma')
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        usuario = auth.authenticate(username=username, password=senha)
    if request.user.is_authenticated:
        return redirect('/index/plataforma')
    if not usuario:
        messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
        return redirect('/auth/logar')
    else:
        auth.login(request, usuario)
        return redirect('/index/plataforma')


def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')