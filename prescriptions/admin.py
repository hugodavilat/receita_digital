from django.contrib import admin

from .models import Receita

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data', 'used')

admin.site.register(Receita, ReceitaAdmin)
