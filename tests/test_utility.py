# tests/test_utility.py

import pytest
from mathlib.utility import factorial, gcd, lcm

def test_factorial():
    """Test the factorial function."""
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(4) == 24
    
    with pytest.raises(ValueError):
        factorial(-1)  # Factorial is not defined for negative integers

def test_gcd():
    """Test the gcd function."""
    assert gcd(48, 18) == 6
    assert gcd(101, 10) == 1
    assert gcd(0, 5) == 5  # GCD of 0 and any positive integer is the positive integer
    assert gcd(10, 10) == 10  # GCD of a number with itself is the number
    
def test_lcm():
    """Test the lcm function."""
    assert lcm(4, 5) == 20
    assert lcm(21, 6) == 42
    assert lcm(0, 10) == 0  # LCM of 0 and any positive integer is 0
    assert lcm(10, 10) == 10  # LCM of a number with itself is the number
