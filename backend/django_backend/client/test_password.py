import pytest
import client.password as passw


def test_password_shorter_than_8():
    assert passw.validate_password('123') is False

def test_password_has_not_supper_char():
    assert passw.validate_password('eight123@') is False

def test_password_has_not_lower_char():
    assert passw.validate_password('EIGHT123@') is False

def test_password_has_not_digit():
    assert passw.validate_password('Eight@@@@') is False

def test_password_has_not_special_char():
    assert passw.validate_password('Eight123') is False

def test_password_correct():
    assert passw.validate_password('Eight123@') is True


