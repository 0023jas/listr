# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-09-19 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentlyWorkingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentCW', models.TextField()),
                ('userName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FinishedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentDone', models.TextField()),
                ('userName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('userName', models.TextField()),
            ],
        ),
    ]
