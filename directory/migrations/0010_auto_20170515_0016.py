# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 22:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0009_auto_20170515_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfc',
            name='cipher_suites',
            field=models.ManyToManyField(blank=True, null=True, to='directory.CipherSuite', verbose_name='Defined cipher suites'),
        ),
        migrations.AlterField(
            model_name='rfc',
            name='obsoleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='obsoleted_set', to='directory.Rfc'),
        ),
        migrations.AlterField(
            model_name='rfc',
            name='obsoletes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='obsoleting_set', to='directory.Rfc'),
        ),
    ]
