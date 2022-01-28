from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Criar todas as classes de acordo com seu diagrama de Classes
class Estado(models.Model):
    sigla = models.CharField(max_length=2, unique=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.sigla + ' - ' + self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome da cidade", )
    habitantes = models.IntegerField(null=True, blank=True, default=0, help_text="Se você não sabe, informe zero.")
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return "{}/{}".format(self.nome, self.estado.sigla)

