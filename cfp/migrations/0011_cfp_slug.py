# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 12:23
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations
from cfp.models import Cfp


def migrate_data_forward(apps, schema_editor):
    for instance in Cfp.cfp.all():
        print("Generating slug for {}".format(instance))
        instance.save()

def migrate_data_backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0010_remove_cfp_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='cfp',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, max_length=255, null=True, populate_from='title', unique=True),
        ),
        migrations.RunPython(
            migrate_data_forward,
            migrate_data_backwards,
        ),
    ]