from django import forms
from finances.models.paymentmethods import PaymentMethods


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethods
        fields = ["nome", "taxa"]
        widgets = {
            "taxa": forms.NumberInput(attrs={"id": "taxa"}),
        }
