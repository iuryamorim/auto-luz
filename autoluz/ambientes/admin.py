from django.contrib import admin
from autoluz.ambientes.models import Ambiente


class AmbienteModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'status')
    search_fields = ('name', 'type', 'status')

admin.site.register(Ambiente, AmbienteModelAdmin)
