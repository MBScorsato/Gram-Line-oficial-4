from django.urls import path
from . import views

urlpatterns = [
    path('index/perfil/meu/mural', views.meu_mural, name='meu_mural'),
]
