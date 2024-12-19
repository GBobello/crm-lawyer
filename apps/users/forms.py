from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users


class UserCreateForm(UserCreationForm):
    password1 = forms.CharField(
        label="Nova Senha",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
        required=False,
    )
    password2 = forms.CharField(
        label="Confirmação da Nova Senha",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
        required=False,
    )

    class Meta:
        model = Users
        fields = [
            "first_name",
            "last_name",
            "username",
            "documento",
            "tipo_pessoa",
            "email",
            "telefone",
            "oab",
            "seccional_oab",
            "estado_civil",
            "endereco",
            "especialidade",
            "password1",
            "password2",
            "nacionalidade",
            "foto",
        ]

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Nome"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Sobrenome"}
            ),
            "username": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Nome de Usuário"}
            ),
            "documento": forms.TextInput(
                attrs={
                    "id": "documento",
                    "class": "form-input",
                    "placeholder": "Documento",
                }
            ),
            "tipo_pessoa": forms.Select(
                attrs={"id": "tipo_pessoa", "class": "form-input px-4 py-2"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-input", "placeholder": "Email"}
            ),
            "telefone": forms.TextInput(
                attrs={
                    "id": "telefone",
                    "class": "form-input",
                    "placeholder": "Telefone",
                }
            ),
            "oab": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Número OAB"}
            ),
            "seccional_oab": forms.Select(
                attrs={"class": "form-input px-4 py-2", "placeholder": "Seccional OAB"}
            ),
            "estado_civil": forms.Select(attrs={"class": "form-input px-4 py-2"}),
            "endereco": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Endereço"}
            ),
            "especialidade": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Especialidade"}
            ),
            "foto": forms.FileInput(attrs={"class": "form-file"}),
            "nacionalidade": forms.TextInput(attrs={"class": "form-input"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check"}),
            "is_superuser": forms.CheckboxInput(attrs={"class": "form-check"}),
        }

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data


class UserEditForm(UserChangeForm):
    password1 = forms.CharField(
        label="Nova Senha",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
        required=False,
    )
    password2 = forms.CharField(
        label="Confirmação da Nova Senha",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
        required=False,
    )

    class Meta:
        model = Users
        fields = [
            "first_name",
            "last_name",
            "username",
            "documento",
            "tipo_pessoa",
            "email",
            "telefone",
            "oab",
            "seccional_oab",
            "estado_civil",
            "endereco",
            "especialidade",
            "nacionalidade",
            "is_active",
            "is_superuser",
            "password1",
            "password2",
            "password",
            "foto",
        ]

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Nome"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Sobrenome"}
            ),
            "username": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Nome de Usuário"}
            ),
            "documento": forms.TextInput(
                attrs={
                    "id": "documento",
                    "class": "form-input",
                    "placeholder": "Documento",
                }
            ),
            "tipo_pessoa": forms.Select(
                attrs={"id": "tipo_pessoa", "class": "form-input px-4 py-2"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-input", "placeholder": "Email"}
            ),
            "telefone": forms.TextInput(
                attrs={
                    "id": "telefone",
                    "class": "form-input",
                    "placeholder": "Telefone",
                }
            ),
            "oab": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Número OAB"}
            ),
            "seccional_oab": forms.Select(
                attrs={"class": "form-input px-4 py-2", "placeholder": "Seccional OAB"}
            ),
            "estado_civil": forms.Select(attrs={"class": "form-input px-4 py-2"}),
            "endereco": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Endereço"}
            ),
            "especialidade": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Especialidade"}
            ),
            "foto": forms.ClearableFileInput(attrs={"class": "form-file"}),
            "nacionalidade": forms.TextInput(attrs={"class": "form-input"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check"}),
            "is_superuser": forms.CheckboxInput(attrs={"class": "form-check"}),
        }

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields.pop("password", None)  # Remove o campo password

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 or password2:  # Se algum campo de senha foi preenchido
            if password1 != password2:
                self.add_error("password2", "As senhas não coincidem.")
        return cleaned_data
