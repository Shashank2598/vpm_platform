# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-20 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='gender',
            field=models.BooleanField(choices=[(True, 'Male'), (False, 'Female')]),
        ),
    ]
