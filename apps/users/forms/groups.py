from django import forms
from django.contrib.auth.models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "permissions"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Nome do Grupo"}
            ),
            "permissions": forms.CheckboxSelectMultiple(),
        }
