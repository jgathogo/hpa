# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='donor_abbrev',
            new_name='abbrev',
        ),
        migrations.AlterField(
            model_name='cfp',
            name='funding_currency',
            field=models.CharField(choices=[('USD', 'US Dollars'), ('GBP', 'British Pound'), ('EUR', 'Euros'), ('KES', 'Kenya Shillings'), ('JPY', 'Japanese Yen'), ('CAD', 'Canadian Dollars')], max_length=3),
        ),
    ]
