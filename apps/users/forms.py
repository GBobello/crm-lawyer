from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users


class UserCreateForm(UserCreationForm):
    class Meta:
        model = Users
        fields = [
            "username",
            "email",
            "telefone",
            "oab",
            "seccional_oab",
            "estado_civil",
            "endereco",
            "especialidade",
            "foto",
            "nacionalidade",
        ]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data


class UserEditForm(UserChangeForm):
    password1 = forms.CharField(
        label="Nova Senha", widget=forms.PasswordInput, required=False
    )
    password2 = forms.CharField(
        label="Confirmação da Nova Senha", widget=forms.PasswordInput, required=False
    )

    class Meta:
        model = Users
        fields = [
            "username",
            "email",
            "telefone",
            "oab",
            "seccional_oab",
            "estado_civil",
            "endereco",
            "especialidade",
            "foto",
            "nacionalidade",
            "is_active",
            "is_superuser",
        ]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 or password2:  # Se algum campo de senha foi preenchido
            if password1 != password2:
                raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data
