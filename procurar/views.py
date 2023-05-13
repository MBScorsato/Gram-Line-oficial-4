from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q

from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q


def procurar(request):
    if request.method == 'GET':
        usuarios = User.objects.all()
        id_usuarios = [usuario.id for usuario in usuarios]  # Obtém os IDs dos usuários

        # Obtém uma lista de todos os IDs dos usuários cadastrados
        # user_ids = User.objects.values_list('id', flat=True)

        # Itera sobre os IDs para teste
        # for user_id in user_ids:
        #    print(user_id)

        return render(request, 'procurar.html', {'usuarios': usuarios, 'id_usuarios': id_usuarios})

    if request.method == 'POST':
        nome_username = request.POST.get('nome_username')  # Obtém o nome de usuário pesquisado do formulário

        # Realiza a pesquisa de usuários com base no nome de usuário fornecido
        usuarios = User.objects.filter(Q(username__icontains=nome_username))

    # Retorne os usuários encontrados para o template
    return render(request, 'procurar.html', {'usuarios': usuarios})


