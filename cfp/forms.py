from django import forms


class EditCfPForm(forms.Form):
    cfp_title = forms.CharField(
        max_length=200, help_text='Enter the call for proposals title, 200 characters max')

    def clean_cfp_title(self):
        data = self.cleaned_data['cfp_title']

        return data