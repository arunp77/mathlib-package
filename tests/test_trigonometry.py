# tests/test_trigonometry.py

import pytest
import math
from mathlib.trigonometry import sin, cos, tan, arcsin, arccos, arctan

def test_sin():
    """Test the sin function."""
    assert sin(math.pi / 2) == pytest.approx(1.0)
    assert sin(0) == pytest.approx(0.0)
    assert sin(math.pi) == pytest.approx(0.0)
    assert sin(-math.pi / 2) == pytest.approx(-1.0)

def test_cos():
    """Test the cos function."""
    assert cos(math.pi) == pytest.approx(-1.0)
    assert cos(0) == pytest.approx(1.0)
    assert cos(math.pi / 2) == pytest.approx(0.0)
    assert cos(-math.pi / 2) == pytest.approx(0.0)

# def test_tan():
#     """Test the tan function."""
#     assert tan(math.pi / 4) == pytest.approx(1.0)
#     assert tan(0) == pytest.approx(0.0)
#     assert tan(-math.pi / 4) == pytest.approx(-1.0)
    
#     # Tan of pi/2 and -pi/2 are undefined but we expect the function to handle it without error
#     assert tan(math.pi / 2) == pytest.approx(float('inf'), rel=1e-2)
#     assert tan(-math.pi / 2) == pytest.approx(float('-inf'), rel=1e-2)

def test_tan():
    """Test the tan function."""
    assert tan(math.pi / 4) == pytest.approx(1.0)
    assert tan(0) == pytest.approx(0.0)
    assert tan(-math.pi / 4) == pytest.approx(-1.0)
    
    # Tan of pi/2 and -pi/2 are undefined; we expect very large positive or negative values
    assert tan(math.pi / 2) > 1e10  # Expect a large positive value
    assert tan(-math.pi / 2) < -1e10  # Expect a large negative value
    

def test_arcsin():
    """Test the arcsin function."""
    assert arcsin(1) == pytest.approx(math.pi / 2)
    assert arcsin(0) == pytest.approx(0.0)
    assert arcsin(-1) == pytest.approx(-math.pi / 2)

    with pytest.raises(ValueError):
        arcsin(2)  # Out of domain

    with pytest.raises(ValueError):
        arcsin(-2)  # Out of domain

def test_arccos():
    """Test the arccos function."""
    assert arccos(1) == pytest.approx(0.0)
    assert arccos(0) == pytest.approx(math.pi / 2)
    assert arccos(-1) == pytest.approx(math.pi)

    with pytest.raises(ValueError):
        arccos(2)  # Out of domain

    with pytest.raises(ValueError):
        arccos(-2)  # Out of domain

def test_arctan():
    """Test the arctan function."""
    assert arctan(1) == pytest.approx(math.pi / 4)
    assert arctan(0) == pytest.approx(0.0)
    assert arctan(-1) == pytest.approx(-math.pi / 4)
    assert arctan(math.inf) == pytest.approx(math.pi / 2)
    assert arctan(-math.inf) == pytest.approx(-math.pi / 2)
