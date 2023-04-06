from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from plataforma.models import Mensagem, FotoPerfil, PontosUsuario


@login_required(login_url='/auth/cadastro')
def indexplataforma(request):
    if request.method == 'GET':
        user = request.user
        username = user.username

        mensagens = Mensagem.objects.all().order_by('-data_criacao')
        imagens = FotoPerfil.objects.filter(usuario_foto=user)

        usuario = request.user
        pontos, created = PontosUsuario.objects.get_or_create(usuario_pontos=usuario)

        context = {
            'mensagens': mensagens,
            'username': username,
            'imagens': imagens,
            'pontos': pontos,
        }
        return render(request, 'plataforma.html', context)

    elif request.method == 'POST':
        mensagem_de_hoje = request.POST.get('mensagem_de_hoje')

        # SE O USUÁRIO NÃO DIGITAR NADA NÃO SALVA E NEM PRINTA NA TELA
        if len(mensagem_de_hoje) == 0:
            return redirect(reverse('indexplataforma'))

        usuario = request.user
        mensagem = Mensagem(mensagem=mensagem_de_hoje, usuario=usuario)
        mensagem.save()
        pontos, created = PontosUsuario.objects.get_or_create(usuario_pontos=usuario)

        usuario = request.user
        pontos.pontos += 1
        pontos.save()
        return redirect(reverse('indexplataforma'))

        # se chegar neste ponto é porque deu tudo certo e o usuário enviou uma mensagem
        # aqui deve-se atribuie +1 na tabela de salvar os pontos


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

    return redirect(reverse('indexperfil'))





