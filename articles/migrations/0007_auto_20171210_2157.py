# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='view_count',
            field=models.PositiveIntegerField(default=0, verbose_name='阅读量'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.Article', verbose_name='文章'),
        ),
    ]
