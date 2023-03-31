from django.urls import path
from . import views

urlpatterns = [
    path('index/plataforma/', views.indexplataforma, name='indexplataforma'),
    path('', views.indexplataforma, name='indexplataforma'),
    path('index/perfil/', views.indexperfil, name='indexperfil'),

]

