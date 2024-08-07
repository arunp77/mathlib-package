# tests/test_random_utils.py

import pytest
import random
from mathlib.random_utils import random_integer, random_float

def test_random_integer():
    """Test the random_integer function."""
    low, high = 1, 10
    for _ in range(100):  # Test with multiple samples to ensure coverage
        result = random_integer(low, high)
        assert low <= result <= high, f"Value {result} not in range [{low}, {high}]"
    
    low, high = -5, 5
    for _ in range(100):
        result = random_integer(low, high)
        assert low <= result <= high, f"Value {result} not in range [{low}, {high}]"

def test_random_float():
    """Test the random_float function."""
    low, high = 1.0, 10.0
    for _ in range(100):  # Test with multiple samples to ensure coverage
        result = random_float(low, high)
        assert low <= result <= high, f"Value {result} not in range [{low}, {high}]"
    
    low, high = -5.0, 5.0
    for _ in range(100):
        result = random_float(low, high)
        assert low <= result <= high, f"Value {result} not in range [{low}, {high}]"
