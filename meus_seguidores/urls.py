from django.urls import path
from . import views

urlpatterns = [
    path('index/perfil/meus/seguidores', views.meus_seguidores, name='meus_seguidores')

]