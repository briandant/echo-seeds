from django import forms
from django.forms.models import inlineformset_factory

from seedbank.models import Seed, Location

# inlineformset_factory creates a Class from a parent model (Seed)
# to a child model (Location)
# SeedLocationFormSet = inlineformset_factory(
#     Seed,
#     Location,
# )

class DateTimeWidget(forms.DateTimeInput):

    def __init__(self, attrs=None):
        if attrs is not None:
            self.attrs = attrs.copy()
        else:
            self.attrs = {'class': 'datepicker'}

        if not 'format' in self.attrs:
            self.attrs['format'] = '%Y-%m-%d'

class SeedForm(forms.ModelForm):

    class Meta:
        model = Seed

        widgets = {
            'aquisition_date': DateTimeWidget()
        }