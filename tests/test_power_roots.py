# tests/test_power_roots.py

import pytest
from mathlib.power_roots import power, sqrt, cbrt

def test_power():
    """Test the power function."""
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(9, 0.5) == pytest.approx(3.0, rel=1e-9)
    assert power(2, -1) == 0.5
    assert power(10, 0) == 1

def test_sqrt():
    """Test the square root function."""
    assert sqrt(4) == 2.0
    assert sqrt(9) == 3.0
    assert sqrt(0) == 0.0
    assert sqrt(1) == 1.0

    # Test for negative input, should raise ValueError
    with pytest.raises(ValueError):
        sqrt(-1)

def test_cbrt():
    """Test the cube root function."""
    assert cbrt(8) == 2.0
    assert cbrt(27) == 3.0
    assert cbrt(-27) == -3.0
    assert cbrt(0) == 0.0
    assert cbrt(1) == 1.0
