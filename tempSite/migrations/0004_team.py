# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tempSite', '0003_league_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('league', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='tempSite.League')),
            ],
        ),
    ]
