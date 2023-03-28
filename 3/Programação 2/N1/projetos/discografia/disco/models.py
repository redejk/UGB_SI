from django.db import models

# Create your models here.
class Discos(models.Model):
    nome = models.CharField('Nome', max_length=200)
    quantidade = models.IntegerField('Quantidade', null=True, blank=True)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)