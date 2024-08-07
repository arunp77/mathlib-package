# tests/test_arithmetic.py

import pytest
from mathlib.arithmetic import add, subtract, multiply, divide, power

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(2, 1) == 1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    with pytest.raises(ValueError):
        power(2, "three")
