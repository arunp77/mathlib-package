# tests/test_logarithmic.py

import pytest
import math
from mathlib.logarithmic import exp, log, log10, log2

def test_exp():
    """Test the exponential function."""
    assert exp(1) == pytest.approx(math.e, rel=1e-9)
    assert exp(0) == 1.0
    assert exp(-1) == pytest.approx(1 / math.e, rel=1e-9)

def test_log():
    """Test the logarithm function with various bases."""
    assert log(10, 10) == 1.0
    assert log(100, 10) == 2.0
    assert log(2) == pytest.approx(math.log(2), rel=1e-9)
    
    # Testing ValueError for invalid inputs
    with pytest.raises(ValueError):
        log(-10, 10)
    
    with pytest.raises(ValueError):
        log(10, 1)
    
    with pytest.raises(ValueError):
        log(10, -10)

def test_log10():
    """Test the base-10 logarithm function."""
    assert log10(100) == 2.0
    assert log10(1) == 0.0
    assert log10(0.1) == -1.0

    # Testing ValueError for invalid inputs
    with pytest.raises(ValueError):
        log10(-10)
        
    with pytest.raises(ValueError):
        log10(0)

def test_log2():
    """Test the base-2 logarithm function."""
    assert log2(8) == 3.0
    assert log2(1) == 0.0
    assert log2(0.5) == -1.0

    # Testing ValueError for invalid inputs
    with pytest.raises(ValueError):
        log2(-10)
        
    with pytest.raises(ValueError):
        log2(0)
