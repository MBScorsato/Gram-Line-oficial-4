from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls')),
    path('', include('plataforma.urls')),
    path('', include('ranking.urls')),
    path('', include('recuperar_senha.urls')),
    path('', include('atualizar_perfil.urls')),
    path('', include('seguindo.urls')),
    path('', include('meus_seguidores.urls')),
    path('', include('meu_mural.urls')),
    path('', include('procurar.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
