from django.db import models

# Create your models here.

class Pessoas(models.Model):
    nome = models.CharField('Nome', max_length=200)
    idade = models.CharField('Telefone', max_length=11)
    telefone = models.IntegerField('Telefone', null=True, blank=True)

    def __str__(self):
        return self.nome