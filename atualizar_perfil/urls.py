from django.urls import path
from atualizar_perfil import views

urlpatterns = [
    path('index/perfil/atualizar/perfil', views.atualizar_perfil, name='atualizar_perfil'),

]
