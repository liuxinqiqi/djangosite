# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20170803_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200, verbose_name='\u5bc6\u7801'),
        ),
    ]
