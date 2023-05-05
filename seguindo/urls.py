from django.urls import path
from seguindo import views

urlpatterns = [
   path('index/perfil/seguindo', views.seguindo, name='seguindo')

]