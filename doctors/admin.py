from django.contrib import admin

from .models import Medico

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('crm', 'nome')

admin.site.register(Medico, MedicoAdmin)

