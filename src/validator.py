"""Common validation helpers for student data."""

import re


_EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$")
_STUDENT_ID_PATTERN = re.compile(r"^[A-Za-z]{2}\d{6}$")


def is_valid_email(value: object) -> bool:
    """Return True for a syntactically valid email address."""
    return isinstance(value, str) and _EMAIL_PATTERN.fullmatch(value) is not None


def is_valid_student_id(value: object) -> bool:
    """Validate an ID containing two letters followed by six digits."""
    return isinstance(value, str) and _STUDENT_ID_PATTERN.fullmatch(value) is not None


def is_non_empty_text(value: object) -> bool:
    """Return True when *value* is a non-empty, non-whitespace string."""
    return isinstance(value, str) and bool(value.strip())


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
