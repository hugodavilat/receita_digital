from django.db import models

from patients.models import Paciente
from main.models import Posologia
from doctors.models import Medico

class Receita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    posologias = models.ManyToManyField(Posologia)
    observacoes = models.TextField(blank=True)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    data = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.medico}, {self.paciente}, {self.data}"

    class Meta:
        db_table = 'receita'
