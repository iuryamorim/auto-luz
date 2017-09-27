# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-12 23:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ambientes', '0003_remove_ambiente_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambientes.Ambiente', verbose_name='Ambiente')),
            ],
            options={
                'verbose_name': 'dispositivo',
                'ordering': ('-created_at',),
                'verbose_name_plural': 'dispositivos',
            },
        ),
    ]