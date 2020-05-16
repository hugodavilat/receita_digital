from django.db import models

# Create your models here.
# Scratch

class Farmacia(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    class Meta:
        db_table = 'farmacia'
    

class Medicamento(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    bula = models.CharField(max_length=200)

    class Meta:
        db_table = 'medicamento'

class Medico(models.Model):
    crm = models.CharField(max_length=100, primary_key=True, unique=True)
    nome = models.CharField(max_length=200, blank=False, null=False)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)

    class Meta:
        db_table = 'medico'

class Paciente(models.Model):
    id_paciente = models.CharField(max_length=100, primary_key=True, unique=True)
    nome = models.CharField(max_length=20, blank=False, null=False)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'paciente'

class Receita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)
    posologia = models.CharField(max_length=30)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    data = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)
    seed = models.CharField(max_length=256)

    class Meta:
        db_table = 'receita'