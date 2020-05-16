from django.db import models

class Farmacia(models.Model):
    nome = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'farmacia'


class Medicamento(models.Model):
    nome = models.CharField(max_length=200, null=False)
    bula = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'medicamento'

class Posologia(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)
    posologia = models.CharField(max_length=30)

    def __str__(self):
        return self.posologia

    class Meta:
        db_table = 'posologia'
