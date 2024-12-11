import re


def remove_special_characters(value: str) -> str:
    return re.sub(r"[\s()./-]", "", value)
