from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash


@login_required
def atualizar_perfil(request):
    if request.method == 'GET':
        email = request.user.email
        username = request.user.username
        return render(request, 'atualizar_perfil.html', {'email': email, 'username': username})
    elif request.method == 'POST':
        email = request.POST.get('email')
        nova_senha = request.POST.get('nova_senha')
        usuario = request.user

        # VERIFICA E INFORMA QUE SENHA TEM QUE TER NO MÍNIMO 6 DIGITOS
        if nova_senha and len(nova_senha.strip()) < 6:
            messages.add_message(request, constants.ERROR, 'A senha tem que ter pelo menos 6 digitos')
            return render(request, 'atualizar_perfil.html',  {'email': email, 'username': usuario.username})

        # VERIFICA E INFORMA QUE O EMAIL É INVÁLIDO
        if email and (not '@' in email or not '.' in email):
            messages.add_message(request, constants.ERROR, 'O email é inválido')
            return render(request, 'atualizar_perfil.html', {'email': email, 'username': usuario.username})

        # ALTERA O EMAIL DO USUÁRIO
        if email and email != usuario.email:
            # verifica se o email já existe
            if User.objects.filter(email=email).exists():
                messages.add_message(request, constants.ERROR, 'O email já está sendo usado por outra pessoa')
                return render(request, 'atualizar_perfil.html', {'email': email, 'username': usuario.username})

            usuario.email = email
            usuario.save()
            messages.add_message(request, constants.SUCCESS, 'Email alterado com sucesso')

        # ALTERA A SENHA DO USUÁRIO
        if nova_senha:
            usuario.set_password(nova_senha)
            usuario.save()
            update_session_auth_hash(request, usuario)
            messages.add_message(request, constants.SUCCESS, 'Senha alterada com sucesso')

        return render(request, 'atualizar_perfil.html', {'email': usuario.email, 'username': usuario.username})
