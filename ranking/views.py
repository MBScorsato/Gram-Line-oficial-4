from django.contrib.auth.models import User
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render


def ranking(request):
    users = User.objects.annotate(pontos=F('pontosusuario__pontos')).filter(pontos__gte=1).order_by('-pontos')
    usuario_logado = request.user
    context = {'users': users, 'usuario_logado': usuario_logado}

    return render(request, 'ranking.html', context)


