from django.contrib import admin
from .models import Paciente

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id_paciente', 'nome')

admin.site.register(Paciente, PacienteAdmin)
