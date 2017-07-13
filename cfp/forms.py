from django import forms
from .models import Cfp


# class EditCfPForm(forms.Form):
#     cfp_title = forms.CharField(
# max_length=200, help_text='Enter the call for proposals title, 200
# characters max')

#     def clean_cfp_title(self):
#         data = self.cleaned_data['cfp_title']

#         return data

class EditCfPForm(forms.ModelForm):
    class Meta:
        model = Cfp
        fields = ['donor', 'cfp_title']




    # donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    # cfp_title = models.CharField(
    #     max_length=200, unique=True, verbose_name='Call for proposals title')
    # cfp_link = models.URLField(verbose_name='Call for proposals website')
    # pub_date = models.DateField(verbose_name='Published')
    # closing_date_provided = models.BooleanField(
    #     verbose_name='Closing date specified?')
    # closing_date = models.DateField(
    #     null=True, blank=True, verbose_name='Closing date for applications')
    # themes = models.ManyToManyField(Theme)
    # zones = models.ManyToManyField(Zone)
    # type_of_projects = models.TextField()
    # # eligibility = models.TextField(verbose_name='Eligibility Criteria')
    # funding_currency = models.CharField(max_length=3, choices=CURRENCY)
    # grant_size_specified = models.BooleanField(
    #     verbose_name='Has the grant size been specified?')
    # overall_budget_specified = models.BooleanField(
    #     verbose_name='Has the overall budget been specified?')
    # overall_budget = models.FloatField(
    #     null=True, blank=True, verbose_name='Total or overall budget available')
    # minimum_budget = models.FloatField(
    #     null=True, blank=True, verbose_name='Minimum budget for a project')
    # maximum_budget = models.FloatField(
    #     null=True, blank=True, verbose_name='Maximum budget for a project')
    # duration_specified = models.BooleanField(
    #     verbose_name='Project duration specified?')
    # duration = models.PositiveIntegerField(
    #     null=True, blank=True, verbose_name='Maximum duration(in months) for a project')
    # # how_to_apply = models.TextField()
    # apply_here = models.URLField(blank=True)
    # notes = models.TextField(blank=True)
