from django import forms
from finances.models.registers import Registers


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
