from django.db import models
from accounts.models import User
from django.db import transaction



class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    crm = models.CharField(max_length=100, primary_key=True, unique=True)
    nome = models.CharField(max_length=200, null=False)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)
    especialidade = models.CharField(max_length=100, blank=True)
    chave_publica = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return self.nome

    @classmethod
    def create(cls, *args, **kwargs):
        with transaction.atomic():
            user = User()
            user.username = kwargs['username']
            user.password = kwargs['password']
            user.user_type=1
            user.save()
            medico = Medico(
                user=user,
                crm=kwargs['id-medico'],
                nome=kwargs['nome'],
                telefone=kwargs['telefone'],
                especialidade=kwargs['especialidade'],
                email=kwargs['email'],
                chave_publica=kwargs['public-key']
            )
            return medico.save()

    class Meta:
        db_table = 'medico'
