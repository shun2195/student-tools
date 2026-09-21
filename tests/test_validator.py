"""Tests for student data validators."""

import pytest

from validator import is_non_empty_text, is_valid_email, is_valid_student_id


@pytest.mark.parametrize("email", ["student@example.com", "a.b+lab@school.edu.vn"])
def test_accepts_valid_email(email):
    assert is_valid_email(email)


@pytest.mark.parametrize("email", ["student", "@example.com", "a@localhost", "", None])
def test_rejects_invalid_email(email):
    assert not is_valid_email(email)


@pytest.mark.parametrize("student_id", ["SV123456", "ab000001"])
def test_accepts_valid_student_id(student_id):
    assert is_valid_student_id(student_id)


@pytest.mark.parametrize("student_id", ["SV12345", "S1234567", "12345678", None])
def test_rejects_invalid_student_id(student_id):
    assert not is_valid_student_id(student_id)


def test_non_empty_text_ignores_surrounding_whitespace():
    assert is_non_empty_text("  hello  ")
    assert not is_non_empty_text("   ")
    assert not is_non_empty_text(None)
