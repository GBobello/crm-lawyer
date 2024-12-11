import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


def validate_phone(value):
    value = re.sub(r"[()./-]", "", value)
    value = re.sub(r"[\s]", "", value)

    if not re.match(r"^(\d{1,3}[- ]?)?\d{10}$", value):
        raise validators.ValidationError(_("Número de telefone inválido."))
    return value
