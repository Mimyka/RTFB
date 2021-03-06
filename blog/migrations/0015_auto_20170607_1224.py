# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 12:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0014_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='status',
        ),
        migrations.AddField(
            model_name='analytic',
            name='User',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='analytic',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='p', max_length=1),
            preserve_default=False,
        ),
    ]
