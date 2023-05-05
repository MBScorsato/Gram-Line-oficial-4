from django.contrib.auth.models import User
from django.shortcuts import render
from plataforma.models import Seguidores, FotoPerfil


def seguindo(request):
    if request.method == 'GET':
        user = request.user
        username = user.username
        user_id = request.user.id

        seguidores_ativos = Seguidores.objects.filter(seguidor=user_id, simounao=True)
        lista_seguidores = []
        for seguidor in seguidores_ativos:
            usuario_seguido = User.objects.get(id=seguidor.id_seguidor)
            lista_seguidores.append(usuario_seguido)

        return render(request, 'seguindo.html', {'seguidores': lista_seguidores})

    if request.method == 'POST':
        return render(request, 'seguindo.html')


