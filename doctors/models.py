from django.db import models

class Medico(models.Model):
    crm = models.CharField(max_length=100, primary_key=True, unique=True)
    nome = models.CharField(max_length=200, null=False)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)
    especialidade = models.CharField(max_length=100, blank=True)
    chave_publica = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'medico'
