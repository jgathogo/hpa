# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 08:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cfp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entered_at', models.DateTimeField(auto_now_add=True)),
                ('cfp_title', models.CharField(max_length=200, unique=True, verbose_name='Call for proposals title')),
                ('cfp_link', models.URLField(verbose_name='Call for proposals website')),
                ('pub_date', models.DateField(verbose_name='Published')),
                ('closing_date_provided', models.BooleanField(verbose_name='Closing date specified?')),
                ('closing_date', models.DateField(blank=True, null=True, verbose_name='Closing date for applications')),
                ('type_of_projects', models.TextField()),
                ('funding_currency', models.CharField(choices=[('USD', 'US Dollars'), ('GBP', 'British Pound'), ('EUR', 'Euro'), ('KES', 'Kenya Shillings'), ('JPY', 'Japanese Yen'), ('CAD', 'Canadian Dollars')], max_length=3)),
                ('grant_size_specified', models.BooleanField(verbose_name='Has the grant size been specified?')),
                ('overall_budget_specified', models.BooleanField(verbose_name='Has the overall budget been specified?')),
                ('overall_budget', models.FloatField(blank=True, null=True, verbose_name='Total or overall budget available')),
                ('minimum_budget', models.FloatField(blank=True, null=True, verbose_name='Minimum budget for a project')),
                ('maximum_budget', models.FloatField(blank=True, null=True, verbose_name='Maximum budget for a project')),
                ('duration_specified', models.BooleanField(verbose_name='Project duration specified?')),
                ('duration', models.PositiveIntegerField(blank=True, null=True, verbose_name='Maximum duration(in months) for a project')),
                ('apply_here', models.URLField(blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            managers=[
                ('cfp', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor', models.CharField(max_length=200, unique=True)),
                ('donor_abbrev', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'ordering': ('donor',),
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ('theme',),
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('zone',),
            },
        ),
        migrations.AddField(
            model_name='cfp',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cfp.Donor'),
        ),
        migrations.AddField(
            model_name='cfp',
            name='themes',
            field=models.ManyToManyField(to='cfp.Theme'),
        ),
        migrations.AddField(
            model_name='cfp',
            name='zones',
            field=models.ManyToManyField(to='cfp.Zone'),
        ),
    ]
