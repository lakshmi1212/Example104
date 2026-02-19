import pytest
from src.math_operations import add

def test_add_integers():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_floats():
    assert add(2.5, 3.1) == pytest.approx(5.6)
    assert add(-1.5, 1.5) == pytest.approx(0.0)

def test_add_int_and_float():
    assert add(2, 3.5) == pytest.approx(5.5)
    assert add(-1.5, 2) == pytest.approx(0.5)

def test_add_invalid_types():
    with pytest.raises(TypeError):
        add('2', 3)
    with pytest.raises(TypeError):
        add(2, None)
    with pytest.raises(TypeError):
        add([1], 2)