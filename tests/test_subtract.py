import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(10, 5) == 5

def test_subtract_negative_numbers():
    assert subtract(-7, -2) == -5

def test_subtract_mixed_sign_numbers():
    assert subtract(10, -3) == 13
    assert subtract(-3, 10) == -13

def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5

def test_subtract_large_numbers():
    assert subtract(3000000, 1000000) == 2000000
