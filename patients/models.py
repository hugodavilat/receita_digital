from django.db import models
from accounts.models import User


class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_paciente = models.CharField(max_length=100, primary_key=True, unique=True)
    nome = models.CharField(max_length=100, null=False)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', blank=True)
    telefone = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'paciente'
