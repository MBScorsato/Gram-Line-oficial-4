from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash

from atualizar_perfil.models import StatusFrase, StatusRelacionamento


@login_required
def atualizar_perfil(request):
    if request.method == 'GET':
        email = request.user.email
        username = request.user.username
        user = request.user
        try:
            frase = StatusFrase.objects.get(status_frase=user).frase
        except StatusFrase.DoesNotExist:
            frase = "Olá! Estou usando a redeGramLine, a melhor rede social que existe :)"
        try:
            opcao_relacionamento = StatusRelacionamento.objects.get(status_relacionamento=user).relacionamento
        except:
            opcao_relacionamento = 'Amizade'
        return render(request, 'atualizar_perfil.html', {
            'email': email,
            'username': username,
            'frase': frase,
            'opcao_relacionamento': opcao_relacionamento
        })

    elif request.method == 'POST':
        email = request.POST.get('email')
        nova_senha = request.POST.get('nova_senha')
        usuario = request.user

        # VERIFICA E INFORMA QUE SENHA TEM QUE TER NO MÍNIMO 6 DIGITOS
        if nova_senha and len(nova_senha.strip()) < 6:
            messages.add_message(request, constants.ERROR, 'A senha tem que ter pelo menos 6 digitos')
            return render(request, 'atualizar_perfil.html', {'email': email, 'username': usuario.username})

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

        # SALVANDO O OPTIUN DO HTML

        # obter o usuário atual
        usuario = request.user
        # obter o status de relacionamento do usuário atual
        status_relacionamento, created = StatusRelacionamento.objects.get_or_create(status_relacionamento=usuario)
        # obter a opção de relacionamento selecionada pelo usuário
        opcao_relacionamento = request.POST.get('relacionamento', f'{status_relacionamento}').strip()
        if opcao_relacionamento is not None:
            status_relacionamento.relacionamento = opcao_relacionamento
        else:
            status_relacionamento.relacionamento = 'Não informado'

        # atualizar o status de relacionamento com a opção selecionada
        status_relacionamento.relacionamento = opcao_relacionamento
        # salvar o status de relacionamento no banco de dados
        status_relacionamento.save()

        # FRASE
        status_frase = None
        try:
            usuario = request.user
            nova_frase = request.POST.get('frase')
            if nova_frase:
                status_frase = StatusFrase.objects.get(status_frase=usuario)
                status_frase.frase = nova_frase
                status_frase.save()

                mensagem = "Frase atualizada com sucesso!"
            else:
                status_frase = StatusFrase.objects.get(status_frase=usuario)
        except StatusFrase.DoesNotExist:
            if nova_frase:
                status_frase = StatusFrase(status_frase=usuario, frase=nova_frase)
                status_frase.save()
                mensagem = "Frase atualizada com sucesso!"
            else:
                mensagem = "Por favor, insira uma frase antes de salvar."

            mensagem = "Frase cadastrada com sucesso!"
        opcao_relacionamento_banco = StatusRelacionamento.objects.get(status_relacionamento=usuario).relacionamento
        return render(request, 'atualizar_perfil.html',
                      {'email': usuario.email,
                       'username': usuario.username,
                       'status_frase': status_frase,
                       'opcao_relacionamento': opcao_relacionamento

                       })
