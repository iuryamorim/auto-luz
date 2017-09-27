from django.db import models

from autoluz.dispositivos.models import Dispositivo
from django.contrib.auth.models import User


class Permissoes(models.Model):
    usuario = models.ForeignKey(User, verbose_name='Usuario')
    dispositivo = models.ForeignKey(Dispositivo, verbose_name='Dispositivo')
    created_at = models.DateTimeField('criado em', auto_now_add = True)

    class Meta:
        verbose_name_plural = 'dispositivos'
        verbose_name = 'dispositivo'
        ordering = ('-created_at',)
