from django import forms
from .models import Suppliers, PaymentMethods, Registers, Frequencies


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


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registers
        fields = [
            "data_abertura",
            "valor_abertura",
            "usuario_abertura",
            "obs",
        ]
        widgets = {
            "data_abertura": forms.DateInput(
                attrs={"id": "data_abertura", "type": "date"}
            ),
            "valor_abertura": forms.NumberInput(attrs={"id": "valor_abertura"}),
            "obs": forms.Textarea(attrs={"id": "obs"}),
        }


class FrequencyForm(forms.ModelForm):
    class Meta:
        model = Frequencies
        fields = ["frequency", "days"]
