from django.contrib import admin
from main.models import Farmacia, Medicamento, Posologia

class FarmaciaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class PosologiaAdmin(admin.ModelAdmin):
    list_display = ('medicamento', 'posologia')

admin.site.register(Farmacia, FarmaciaAdmin)
admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Posologia, PosologiaAdmin)
