# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-19 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180619_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanfran',
            name='Day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=10),
        ),
        migrations.AlterField(
            model_name='sanfran',
            name='Location',
            field=models.CharField(choices=[('BAYVIEW', 'BAYVIEW'), ('CENTRAL', 'CENTRAL'), ('INGLESIDE', 'INGLESIDE'), ('MISSION', 'MISSION'), ('NORTHERN', 'NORTHERN'), ('PARK', 'PARK'), ('RICHMOND', 'RICHMOND'), ('SOUTHERN', 'SOUTHERN'), ('TARAVAL', 'TARAVAL'), ('TENDERLOIN', 'TENDERLOIN')], max_length=20),
        ),
    ]
