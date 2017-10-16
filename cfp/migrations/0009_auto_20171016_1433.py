# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 11:33
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0008_cfp_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cfp',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]