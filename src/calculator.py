"""Basic calculator operations with input validation."""

from numbers import Real


def _validate_number(value: Real, name: str) -> None:
    """Raise TypeError when *value* is not a real number."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{name} must be a real number")


def add(a: Real, b: Real) -> Real:
    """Return the sum of two real numbers."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a + b


def subtract(a: Real, b: Real) -> Real:
    """Return *b* subtracted from *a*."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a - b


def multiply(a: Real, b: Real) -> Real:
    """Return the product of two real numbers."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a * b


def divide(a: Real, b: Real) -> float:
    """Return *a / b* or raise ValueError when *b* is zero."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
