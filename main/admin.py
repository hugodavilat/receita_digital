from django.contrib import admin
from main import models

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id_paciente', 'nome')

admin.site.register(models.Farmacia)
admin.site.register(models.Medicamento)
admin.site.register(models.Medico)
admin.site.register(models.Paciente, PacienteAdmin)
admin.site.register(models.Posologia)
admin.site.register(models.Receita)
