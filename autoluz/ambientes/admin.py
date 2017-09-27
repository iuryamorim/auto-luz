from django.contrib import admin
from autoluz.ambientes.models import Ambiente


class AmbienteModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Ambiente, AmbienteModelAdmin)
