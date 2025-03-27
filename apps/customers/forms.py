from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "nome",
            "documento",
            "rg",
            "telefone",
            "email",
            "tipo_pessoa",
            "data_nascimento",
            "nacionalidade",
            "estado_civil",
            "profissao",
            "genitor",
            "genitora",
            "cep",
            "endereco",
            "numero",
            "complemento",
            "bairro",
            "cidade",
            "estado",
            "ativo",
        ]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-input"}),
            "documento": forms.TextInput(
                attrs={"id": "documento", "class": "form-input"}
            ),
            "rg": forms.TextInput(attrs={"class": "form-input"}),
            "telefone": forms.TextInput(
                attrs={"id": "telefone", "class": "form-input"}
            ),
            "email": forms.EmailInput(attrs={"class": "form-input"}),
            "tipo_pessoa": forms.Select(
                attrs={"id": "tipo_pessoa", "class": "form-input px-4 py-2"}
            ),
            "data_nascimento": forms.TextInput(
                attrs={"id": "data", "type": "date", "class": "form-input"}
            ),
            "nacionalidade": forms.TextInput(attrs={"class": "form-input"}),
            "estado_civil": forms.Select(attrs={"class": "form-input px-4 py-2"}),
            "profissao": forms.TextInput(attrs={"class": "form-input"}),
            "genitor": forms.TextInput(attrs={"class": "form-input"}),
            "genitora": forms.TextInput(attrs={"class": "form-input"}),
            "cep": forms.TextInput(
                attrs={"id": "cep", "onblur": "buscarCep()", "class": "form-input"}
            ),
            "endereco": forms.TextInput(
                attrs={"id": "endereco", "class": "form-input"}
            ),
            "numero": forms.TextInput(attrs={"class": "form-input"}),
            "complemento": forms.TextInput(attrs={"class": "form-input"}),
            "bairro": forms.TextInput(attrs={"id": "bairro", "class": "form-input"}),
            "cidade": forms.TextInput(attrs={"id": "cidade", "class": "form-input"}),
            "estado": forms.Select(attrs={"class": "form-input px-4 py-2"}),
            "ativo": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }
