from django.db import models


class Ambiente(models.Model):
    name = models.CharField('nome', max_length=255)
    created_at = models.DateTimeField('criado em', auto_now_add = True)

    class Meta:
        verbose_name_plural = 'ambientes'
        verbose_name = 'ambiente'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
