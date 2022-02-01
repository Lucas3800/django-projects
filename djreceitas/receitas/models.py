from django.db import models
from datetime import datetime
from pessoas.models import *


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome

class Receita(models.Model):
    nome = models.CharField(max_length=200, help_text='Nome da receita')
    ingredientes = models.TextField(help_text='Ingredientes utilizados na receita')
    modo_preparo = models.TextField(help_text='Modo de preparo da receita')
    tempo_preparo = models.IntegerField(help_text='Tempo de preparo da receita em minutos. (Ex: 10 minutos)')
    rendimento = models.CharField(max_length=100, help_text='Rendimento da receita. (Ex: 5 porções')
    data_receita = models.DateTimeField(default=datetime.now, blank=True, help_text='Data de postagem da receita')
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, help_text='Categoria da receira. (Ex: SOPAS|CARNES|SUCOS)')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING, help_text='Pessoa a postar a receita', default=1)

    def __str__(self) -> str:
        return self.nome