from django.db import models

#criar tabelas
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    idade = models.IntegerField()
    ativo = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nome

