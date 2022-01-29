from django.db import models
from datetime import datetime


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome

class Receita(models.Model):
    nome = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome