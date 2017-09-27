from django.db import models

from autoluz.ambientes.models import Ambiente


class Dispositivo(models.Model):
    name = models.CharField('nome', max_length=255)
    ambiente = models.ForeignKey(Ambiente, verbose_name='Ambiente')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField('criado em', auto_now_add = True)

    class Meta:
        verbose_name_plural = 'dispositivos'
        verbose_name = 'dispositivo'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
