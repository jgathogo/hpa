# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 10:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0003_auto_20171016_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cfp',
            old_name='cfp_link',
            new_name='link',
        ),
    ]
