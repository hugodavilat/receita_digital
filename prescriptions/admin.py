from django.contrib import admin

from .models import Receita

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'medico', 'data', 'used')
    list_display_links = ('id', 'paciente')
    readonly_fields = ('id',)

admin.site.register(Receita, ReceitaAdmin)
