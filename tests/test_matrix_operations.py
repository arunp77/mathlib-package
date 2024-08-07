# tests/test_matrix_operations.py

import pytest
import numpy as np
from mathlib.matrix_operations import matrix_addition, matrix_multiplication, matrix_determinant, matrix_inverse

def test_matrix_addition():
    """Test addition of two matrices."""
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    expected = np.array([[6, 8], [10, 12]])
    assert np.array_equal(matrix_addition(matrix1, matrix2), expected)

def test_matrix_multiplication():
    """Test multiplication of two matrices."""
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    expected = np.array([[19, 22], [43, 50]])
    assert np.array_equal(matrix_multiplication(matrix1, matrix2), expected)

def test_matrix_determinant():
    """Test computation of the matrix determinant."""
    matrix = np.array([[1, 2], [3, 4]])
    expected = -2.0
    assert matrix_determinant(matrix) == pytest.approx(expected, rel=1e-9)

def test_matrix_inverse():
    """Test computation of the matrix inverse."""
    matrix = np.array([[1, 2], [3, 4]])
    expected = np.array([[-2.0, 1.0], [1.5, -0.5]])
    assert np.allclose(matrix_inverse(matrix), expected, rtol=1e-9)

    # Test for a singular matrix (should raise a LinAlgError)
    singular_matrix = np.array([[1, 2], [2, 4]])
    with pytest.raises(np.linalg.LinAlgError):
        matrix_inverse(singular_matrix)
