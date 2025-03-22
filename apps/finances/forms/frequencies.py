from django import forms
from finances.models.frequencies import Frequencies


class FrequencyForm(forms.ModelForm):
    class Meta:
        model = Frequencies
        fields = ["frequency", "days"]
