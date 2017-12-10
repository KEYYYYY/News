# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 23:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20171209_2328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-add_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterField(
            model_name='article',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='发表日期'),
        ),
    ]
