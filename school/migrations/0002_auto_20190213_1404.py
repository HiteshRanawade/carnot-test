# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-13 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='schools',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='students',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='books',
            name='no_of_pages',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]
