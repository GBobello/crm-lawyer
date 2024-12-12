from django import forms
from .models import Suppliers


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
