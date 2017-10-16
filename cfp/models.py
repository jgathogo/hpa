import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse
from autoslug import AutoSlugField


class Donor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    abbrev = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.abbrev

    class Meta:
        ordering = ('name',)


class Theme(models.Model):
    theme = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.theme

    class Meta:
        ordering = ('theme',)


class Zone(models.Model):
    zone = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.zone

    class Meta:
        ordering = ('zone',)


class Cfp(models.Model):
    CURRENCY = (
        ('USD', 'US Dollars'),
        ('GBP', 'British Pound'),
        ('EUR', 'Euros'),
        ('KES', 'Kenya Shillings'),
        ('JPY', 'Japanese Yen'),
        ('CAD', 'Canadian Dollars'),
    )
    entered_at = models.DateTimeField(auto_now_add=True, editable=False)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=200, unique=True, verbose_name='Call for proposals title')
    slug = AutoSlugField(max_length=255, null=True, editable=True, unique=True, populate_from='title')
    link = models.URLField(verbose_name='Call for proposals website')
    pub_date = models.DateField(verbose_name='Published')
    closing_date_provided = models.BooleanField(
        verbose_name='Closing date specified?')
    closing_date = models.DateField(
        null=True, blank=True, verbose_name='Closing date for applications')
    themes = models.ManyToManyField(Theme)
    zones = models.ManyToManyField(Zone)
    type_of_projects = models.TextField()
    # eligibility = models.TextField(verbose_name='Eligibility Criteria')
    funding_currency = models.CharField(max_length=3, choices=CURRENCY)
    grant_size_specified = models.BooleanField(
        verbose_name='Has the grant size been specified?')
    overall_budget_specified = models.BooleanField(
        verbose_name='Has the overall budget been specified?')
    overall_budget = models.FloatField(
        null=True, blank=True, verbose_name='Total or overall budget available')
    minimum_budget = models.FloatField(
        null=True, blank=True, verbose_name='Minimum budget for a project')
    maximum_budget = models.FloatField(
        null=True, blank=True, verbose_name='Maximum budget for a project')
    duration_specified = models.BooleanField(
        verbose_name='Project duration specified?')
    duration = models.PositiveIntegerField(
        null=True, blank=True, verbose_name='Maximum duration(in months) for a project')
    # how_to_apply = models.TextField()
    apply_here = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('cfp:cfp_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    def past_deadline(self):
        # leo = datetime.date.today()
        # deadline = self.closing_date
        # return leo > deadline
        pass

    def no_closing_date(self):
        return self.closing_date is None

    cfp = models.Manager()
