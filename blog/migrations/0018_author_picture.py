# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20170607_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='picture',
            field=models.ImageField(default=' ', upload_to=b''),
            preserve_default=False,
        ),
    ]
