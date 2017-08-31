from django.db import models


class Ambiente(models.Model):
    name = models.CharField('nome', max_length=255)
    type = models.CharField('tipo', max_length=150, choices = [('sala_de_aula', 'Sala de aula'),
                    ('sala_dos_professores', 'Sala dos Professores'), ('corredor', 'Corredor')])
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField('criado em', auto_now_add = True)

    class Meta:
        verbose_name_plural = 'ambientes'
        verbose_name = 'ambiente'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
