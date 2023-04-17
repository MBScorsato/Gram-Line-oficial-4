from django.urls import path
from . import views

urlpatterns = [
    path('index/plataforma/', views.indexplataforma, name='indexplataforma'),
    path('', views.indexplataforma, name='indexplataforma'),
    path('index/perfil/', views.indexperfil, name='indexperfil'),
    path('index/perfil/user/<int:user_id>/', views.ver_perfil_user, name='ver_perfil_user'),

]

