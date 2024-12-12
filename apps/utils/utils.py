import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


def remove_special_characters(value: str) -> str:
    return re.sub(r"[\s()./-]", "", value)


def validate_phone(value):
    value = re.sub(r"[()./-]", "", value)
    value = re.sub(r"[\s]", "", value)

    if not re.match(r"^(\d{1,3}[- ]?)?\d{10}$", value):
        raise validators.ValidationError(_("Número de telefone inválido."))

    return value


def validate_document(value):
    value = re.sub(r"[()./-]", "", value)
    value = re.sub(r"[\s]", "", value)

    if not re.match(
        r"^([0-9]{11})$|^([0-9]{14})$",
        value,
    ):
        raise validators.ValidationError(_("Documento inválido."))
    else:
        if len(value) == 11:
            if value == value[0] * len(value):
                raise validators.ValidationError(_("Documento inválido."))
            else:
                for i in range(9, 11):
                    soma = sum(int(value[j]) * (i + 1 - j) for j in range(i))
                    digito = (soma * 10 % 11) % 10
                    if digito != int(value[i]):
                        raise validators.ValidationError(_("Documento inválido."))
        elif len(value) == 14:
            if value == value[0] * len(value):
                raise validators.ValidationError(_("Documento inválido."))
            else:
                pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
                pesos_2 = [6] + pesos_1

                for i in range(12, 14):
                    soma = (
                        sum(int(value[j]) * pesos_1[j] for j in range(i))
                        if i == 12
                        else sum(int(value[j]) * pesos_2[j] for j in range(i))
                    )
                    digito = soma % 11
                    digito = 0 if digito < 2 else 11 - digito
                    if digito != int(value[i]):
                        raise validators.ValidationError(_("Documento inválido."))

    return value


def telefone_formatado(value: str) -> str:
    # Usando uma expressão regular para formatar o telefone
    value = re.sub(r"(\d{2})(\d{5})(\d{4})", r"(\1) \2-\3", value)
    return value
