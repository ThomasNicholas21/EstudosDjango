from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Agenda(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    data_agenda = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(
        auto_now=True, verbose_name='Data da Criacao')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
