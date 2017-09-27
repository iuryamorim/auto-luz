from django.contrib import admin
from autoluz.dispositivos.models import Dispositivo


class DispositivoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'ambiente', 'status')
    search_fields = ('name', 'ambiente', 'status')

admin.site.register(Dispositivo, DispositivoModelAdmin)
