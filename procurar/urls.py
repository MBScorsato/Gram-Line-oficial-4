from django.urls import path
from . import views

urlpatterns = [
    path('index/perfil/procurar/', views.procurar, name='procurar'),
    # path('index/perfil/procurar/', views.procurar, name='procurar')

]