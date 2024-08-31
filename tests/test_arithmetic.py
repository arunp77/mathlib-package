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

#------------------ unittest-----------------------------------------
# # tests/test_arithmetic.py
# import unittest
# from mathlib import arithmetic

# class TestArithmetic(unittest.TestCase):
#     """Unit tests for arithmetic operations."""

#     def test_add(self):
#         """Test the add function."""
#         self.assertEqual(arithmetic.add(2, 3), 5)
#         self.assertEqual(arithmetic.add(-1, 1), 0)
#         self.assertAlmostEqual(arithmetic.add(2.5, 3.5), 6.0)

#     def test_subtract(self):
#         """Test the subtract function."""
#         self.assertEqual(arithmetic.subtract(5, 3), 2)
#         self.assertEqual(arithmetic.subtract(0, 5), -5)
#         self.assertAlmostEqual(arithmetic.subtract(2.5, 1.5), 1.0)

#     def test_multiply(self):
#         """Test the multiply function."""
#         self.assertEqual(arithmetic.multiply(2, 3), 6)
#         self.assertEqual(arithmetic.multiply(-1, 5), -5)
#         self.assertAlmostEqual(arithmetic.multiply(2.5, 4), 10.0)

#     def test_divide(self):
#         """Test the divide function."""
#         self.assertAlmostEqual(arithmetic.divide(6, 3), 2.0)
#         self.assertAlmostEqual(arithmetic.divide(5, 2), 2.5)
#         with self.assertRaises(ZeroDivisionError):
#             arithmetic.divide(5, 0)

# if __name__ == '__main__':
#     unittest.main()

#----------------- doctest ------------------
# # mathlib/arithmetic.py

# # ... [existing code] ...

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
