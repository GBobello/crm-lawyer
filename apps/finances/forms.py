from django import forms
from .models import Suppliers, PaymentMethods


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = [
            "nome",
            "documento",
            "telefone",
            "email",
            "endereco",
        ]
        widgets = {
            "documento": forms.TextInput(attrs={"id": "documento"}),
            "telefone": forms.TextInput(attrs={"id": "telefone"}),
        }


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethods
        fields = ["nome", "taxa"]
        widgets = {
            "taxa": forms.NumberInput(attrs={"id": "taxa"}),
        }
