# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_author_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
