from django.contrib import admin
from plataforma.models import Mensagem, FotoPerfil, UltimaMensagem


# Register your models here.
admin.site.register(Mensagem)
admin.site.register(UltimaMensagem)
admin.site.register(FotoPerfil)
