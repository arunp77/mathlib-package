# tests/test_complex_numbers.py

import pytest
import cmath
from mathlib.complex_numbers import (
    complex_addition,
    complex_subtraction,
    complex_multiplication,
    complex_division,
    complex_magnitude,
    complex_phase
)

def test_complex_addition():
    assert complex_addition(1 + 2j, 3 + 4j) == (4 + 6j)

def test_complex_subtraction():
    assert complex_subtraction(5 + 6j, 3 + 2j) == (2 + 4j)

def test_complex_multiplication():
    assert complex_multiplication(1 + 2j, 3 + 4j) == (-5 + 10j)

def test_complex_division():
    assert complex_division(1 + 2j, 3 + 4j) == pytest.approx(0.44 + 0.08j, rel=1e-2)

def test_complex_magnitude():
    assert complex_magnitude(3 + 4j) == 5.0

def test_complex_phase():
    assert complex_phase(1 + 1j) == pytest.approx(cmath.phase(1 + 1j), rel=1e-9)
