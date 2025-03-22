from django import forms
from finances.models.providedservices import ProvidedServices


class ProvidedServicesForm(forms.ModelForm):
    class Meta:
        model = ProvidedServices
        fields = ["nome"]
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Nome"}
            ),
        }
