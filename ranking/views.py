from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render

from plataforma.models import PontosUsuario


@login_required(login_url='/auth/cadastro')
def indexranking(request):
    users = User.objects.annotate(pontos=F('pontosusuario__pontos')).filter(pontos__gte=1).order_by('-pontos')
    usuario_logado = request.user

    pontos_do_usuario = PontosUsuario.objects.get(usuario_pontos=usuario_logado).pontos

    context = {'users': users, 'usuario_logado': usuario_logado, 'pontos_do_usuario': pontos_do_usuario}

    return render(request, 'indexranking.html', context)





