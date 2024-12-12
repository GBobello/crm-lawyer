import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

from utils import utils


def validate_phone(value):
    return utils.validate_phone(value)
