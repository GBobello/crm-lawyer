from django import forms
from finances.models.suppliers import Suppliers


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
