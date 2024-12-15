from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "nome",
            "documento",
            "telefone",
            "email",
            "tipo_pessoa",
            "data_nascimento",
            "cep",
            "endereco",
            "numero",
            "complemento",
            "bairro",
            "cidade",
            "estado",
            "rg",
            "genitor",
            "genitora",
            "profissao",
            "nacionalidade",
            "estado_civil",
        ]
        widgets = {
            "documento": forms.TextInput(attrs={"id": "documento"}),
            "telefone": forms.TextInput(attrs={"id": "telefone"}),
            "data_nascimento": forms.TextInput(attrs={"id": "data", "type": "date"}),
            "cep": forms.TextInput(attrs={"id": "cep", "onblur": "buscarCep()"}),
            "endereco": forms.TextInput(attrs={"id": "endereco"}),
            "bairro": forms.TextInput(attrs={"id": "bairro"}),
            "cidade": forms.TextInput(attrs={"id": "cidade"}),
            "tipo_pessoa": forms.Select(attrs={"id": "tipo_pessoa"}),
        }
