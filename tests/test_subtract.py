import pytest
from src.math_operations import subtract

def test_subtract_integers():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(-5, 3) == -8

def test_subtract_floats():
    assert subtract(5.5, 2.2) == pytest.approx(3.3)
    assert subtract(-1.1, -2.2) == pytest.approx(1.1)

def test_subtract_int_and_float():
    assert subtract(5, 2.5) == pytest.approx(2.5)
    assert subtract(-2.5, 5) == pytest.approx(-7.5)

def test_subtract_invalid_types():
    with pytest.raises(TypeError):
        subtract('5', 3)
    with pytest.raises(TypeError):
        subtract(5, None)
    with pytest.raises(TypeError):
        subtract([1], 2)