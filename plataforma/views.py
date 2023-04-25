from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta
from atualizar_perfil.models import StatusFrase
from plataforma.models import Mensagem, FotoPerfil, PontosUsuario, UltimaMensagem, PropagandaUm
from django.contrib.messages import constants


@login_required(login_url='/auth/cadastro')
def indexplataforma(request):
    if request.method == 'GET':
        user = request.user
        username = user.username

        mensagens = Mensagem.objects.all().order_by('-data_criacao')
        imagens = FotoPerfil.objects.filter(usuario_foto=user)

        usuario = request.user
        pontos, created = PontosUsuario.objects.get_or_create(usuario_pontos=usuario)

        propagandas = PropagandaUm.objects.all()

        context = {
            #'frase': frase,
            'mensagens': mensagens,
            'username': username,
            'imagens': imagens,
            'pontos': pontos,
            'propagandas': propagandas,
        }
        return render(request, 'plataforma.html', context)

    elif request.method == 'POST':

        # verifica se existe alguma mensagem na base de dados
        ultima_mensagem, created = UltimaMensagem.objects.get_or_create(usuario=request.user)

        # Obtenha a data da ultima mensagem com fuso horário definido
        data_ultima_mensagem = ultima_mensagem.data_ultima_mensagem.astimezone()

        # Obtenha a data atual com fuso horário definido
        data_atual = timezone.now()

        # Calcule a diferença de tempo
        diferenca = data_atual - data_ultima_mensagem

        # Compare se a diferença é menor a uma hora
        if diferenca < timedelta(hours=1):
            restante = (timedelta(hours=1) - diferenca).total_seconds() // 60
            messages.add_message(request, constants.ERROR,
                                 f'Você precisa esperar mais {int(restante)} minutos')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        mensagem_de_hoje = request.POST.get('mensagem_de_hoje')

        # SE O USUÁRIO NÃO DIGITAR NADA NÃO SALVA E NEM PRINTA NA TELA

        if len(mensagem_de_hoje) == 0:
            return redirect('indexplataforma')

        usuario = request.user

        mensagem = Mensagem(mensagem=mensagem_de_hoje, usuario=usuario)

        mensagem.save()

        pontos, created = PontosUsuario.objects.get_or_create(usuario_pontos=usuario)

        pontos.pontos += 1

        pontos.save()

        ultima_mensagem.atualizar_data_ultima_mensagem()

        return redirect('indexplataforma')


@login_required(login_url='/auth/cadastro')
def indexperfil(request):
    if request.method == 'GET':
        imagens = FotoPerfil.objects.filter(usuario_foto=request.user)

        context = {
            'imagens': imagens,
        }
        return render(request, 'indexperfil.html', context)

    elif request.method == 'POST':
        file = request.FILES.get('imagem')
        usuario = request.user

        # verifica se já existe uma imagem de perfil para o usuário e a atualiza ou cria uma nova
        imagem_usuario, created = FotoPerfil.objects.get_or_create(usuario_foto=usuario)
        if not created:
            imagem_usuario.foto.delete()
        imagem_usuario.foto = file
        imagem_usuario.save()
        return redirect(reverse('indexperfil'))


@login_required(login_url='/auth/cadastro')
def ver_perfil_user(request, user_id):
    if request.method == 'GET':
        # Busca o usuário com o user_id correspondente ou retorna uma página 404 se não encontrado
        usuario = get_object_or_404(User, pk=user_id)
        foto = FotoPerfil.objects.filter(usuario_foto=usuario).first()
        pontos_usuario = PontosUsuario.objects.get(usuario_pontos=usuario)
        pontos = pontos_usuario.pontos

        usuario = request.user
        try:
            frase = StatusFrase.objects.get(status_frase=user_id)
        except:
            frase = ''

        context = {'usuario': usuario,
                   'frase': frase,
                   'foto': foto,
                   'pontos': pontos}
        return render(request, 'ver_perfil_user.html', context)

    elif request.method == 'POST':
        return render(request, 'ver_perfil_user.html')
