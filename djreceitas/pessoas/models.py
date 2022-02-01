from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=255, help_text='Nome do usuário')
    email = models.EmailField(max_length=200, help_text='E-mail do usuário (Ex: exemplo@dominio.com')

    def __str__(self) -> str:
        return self.nome
