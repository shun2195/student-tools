"""Tests for calculator operations."""

import pytest

from calculator import add, divide, multiply, subtract


def test_basic_operations():
    assert add(2, 3) == 5
    assert subtract(7, 4) == 3
    assert multiply(3, 5) == 15
    assert divide(10, 2) == 5


def test_operations_support_negative_and_float_values():
    assert add(-2, 0.5) == pytest.approx(-1.5)
    assert multiply(-3, -2) == 6


def test_divide_by_zero_returns_meaningful_error():
    with pytest.raises(ValueError,match=" divide by zero"):
        divide(10,0)


@pytest.mark.parametrize("invalid", ["2", None, True])
def test_rejects_non_numeric_input(invalid):
    with pytest.raises(TypeError):
        add(invalid, 2)
