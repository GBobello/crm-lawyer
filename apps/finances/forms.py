from django import forms
from .models import Suppliers, PaymentMethods, Registers, Frequencies, ProvidedServices


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
            "nome": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Nome"}
            ),
            "documento": forms.TextInput(
                attrs={
                    "id": "documento",
                    "class": "form-input",
                    "placeholder": "Documento",
                }
            ),
            "telefone": forms.TextInput(
                attrs={
                    "id": "telefone",
                    "class": "form-input",
                    "placeholder": "Telefone",
                }
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-input ", "placeholder": "Email"}
            ),
            "endereco": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Endereço"}
            ),
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


class ProvidedServicesForm(forms.ModelForm):
    class Meta:
        model = ProvidedServices
        fields = ["nome"]
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Nome"}
            ),
        }
