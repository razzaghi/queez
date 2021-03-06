# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-15 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graphQl', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='question_name',
        ),
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.ManyToManyField(related_name='options_set', to='graphQl.option'),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_option',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='correct_option_set', to='graphQl.option'),
        ),
    ]
