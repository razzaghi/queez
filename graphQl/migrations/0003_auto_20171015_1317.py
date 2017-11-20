# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-15 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graphQl', '0002_auto_20171015_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=b'unknown', max_length=20)),
                ('image', models.ImageField(default=b'anonymous.jpg', upload_to=b'uploads/story/')),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default=b'anonymous.jpg', upload_to=b'uploads/category/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(default=b'unknown', max_length=20),
        ),
        migrations.AddField(
            model_name='story',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graphQl.category'),
        ),
    ]