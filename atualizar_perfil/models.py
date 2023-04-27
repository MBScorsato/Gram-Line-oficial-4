from django.contrib.auth.models import User
from django.db import models


class StatusFrase(models.Model):
    status_frase = models.ForeignKey(User, on_delete=models.CASCADE)
    frase = models.CharField(max_length=255)

    def  __str__(self):
        return self.frase


class StatusRelacionamento(models.Model):
    status_relacionamento = models.ForeignKey(User, on_delete=models.CASCADE)
    relacionamento = models.CharField(max_length=30)

    def __str__(self):
        return self.relacionamento

