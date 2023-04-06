from django.db import models
from django.contrib.auth.models import User


class Mensagem(models.Model):
    mensagem = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.usuario}: {self.mensagem}"


class FotoPerfil(models.Model):
    usuario_foto = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to='img')


class PontosUsuario(models.Model):
    usuario_pontos = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pontos = models.IntegerField(default=0)

