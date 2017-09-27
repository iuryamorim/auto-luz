from django.contrib import admin
from autoluz.permissoes.models import Permissoes


class PermissoesModelAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'dispositivo')
    search_fields = ('usuario', 'dispositivo')

admin.site.register(Permissoes, PermissoesModelAdmin)
