# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_analytic_part_concerned'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DecimalField(blank=True, decimal_places=0, default=2000, max_digits=4),
            preserve_default=False,
        ),
    ]
