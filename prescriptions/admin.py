from django.contrib import admin

from .models import Receita

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data', 'used')
    readonly_fields = ('id',)

admin.site.register(Receita, ReceitaAdmin)
