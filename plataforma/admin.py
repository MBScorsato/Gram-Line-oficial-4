from django.contrib import admin
from plataforma.models import Mensagem, FotoPerfil, UltimaMensagem, PropagandaUm


# Register your models here.
admin.site.register(Mensagem)
admin.site.register(UltimaMensagem)
admin.site.register(PropagandaUm)
admin.site.register(FotoPerfil)
