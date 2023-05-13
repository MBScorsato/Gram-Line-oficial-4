from django.shortcuts import render


def meu_mural(request):
    if request.method == 'GET':
        return render(request, 'meu_mural.html')
