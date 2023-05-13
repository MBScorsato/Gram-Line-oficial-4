from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from plataforma.models import Seguidores


@login_required(login_url='/auth/cadastro')
def meus_seguidores(request):
    if request.method == 'GET':
        # Obter o usuário conectado
        user = request.user

        # Filtrar os objetos Seguidores pelo usuário seguido
        seguidores = Seguidores.objects.filter(id_seguidor=user.id)

        # Obter uma lista de usuários correspondentes aos seguidores
        usuarios_seguidores = [seguidor.seguidor for seguidor in seguidores]
        print(usuarios_seguidores)

        return render(request, 'meus_seguidores.html', {'usuarios_seguidores': usuarios_seguidores})