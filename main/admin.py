from django.contrib import admin
from main import models

admin.site.register(models.Farmacia)
admin.site.register(models.Medicamento)
admin.site.register(models.Medico)
admin.site.register(models.Paciente)
admin.site.register(models.Receita)