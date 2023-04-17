from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class UltimaMensagem(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_ultima_mensagem = models.DateTimeField(default=timezone.now)

    def atualizar_data_ultima_mensagem(self):
        self.data_ultima_mensagem = timezone.now()
        self.save()

    def __str__(self):
        return self.usuario.username


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


class PropagandaUm(models.Model):
    nome_empresa = models.CharField(max_length=100)
    imagem_empresa = models.ImageField(upload_to='imagem_empresa')
    texto_empresa = models.CharField(max_length=500)
    link_empresa = models.CharField(max_length=500)
    ativar_propaganda = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_empresa


