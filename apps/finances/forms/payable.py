from django import forms
from finances.models.payable import Payable


class PayableForm(forms.ModelForm):
    class Meta:
        model = Payable
        fields = [
            "description",
            "value",
            "supplier",
            "due_date",
            "payment_date",
            "payment_method",
            "frequency",
            "obs",
        ]
        widgets = {
            "description": forms.TextInput(attrs={"id": "description"}),
            "value": forms.NumberInput(attrs={"id": "value"}),
            "supplier": forms.Select(attrs={"id": "supplier"}),
            "due_date": forms.DateInput(attrs={"id": "due_date"}),
            "payment_date": forms.DateInput(attrs={"id": "payment_date"}),
            "payment_method": forms.Select(attrs={"id": "payment_method"}),
            "frequency": forms.Select(attrs={"id": "frequency"}),
            "obs": forms.Textarea(attrs={"id": "obs"}),
        }
