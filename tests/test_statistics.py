# tests/test_statistics.py

import pytest
from mathlib.statistics import mean, median, variance, standard_deviation

def test_mean():
    """Test the mean function."""
    assert mean([1, 2, 3, 4, 5]) == 3.0
    assert mean([10, 20, 30]) == 20.0
    assert mean([1, 1, 1, 1]) == 1.0
    assert mean([2.5, 3.5, 4.5]) == 3.5

    with pytest.raises(ValueError):
        mean([])

def test_median():
    """Test the median function."""
    assert median([1, 2, 3, 4, 5]) == 3.0
    assert median([1, 3, 3, 6, 7, 8, 9]) == 6.0
    assert median([2, 3, 4, 5, 6]) == 4.0
    assert median([1, 2]) == 1.5

    with pytest.raises(ValueError):
        median([])


def test_variance():
    """Test the variance function."""
    assert variance([1, 2, 3, 4, 5]) == 2.5
    assert variance([10, 20, 30]) == 100.0
    assert variance([1, 1, 1, 1]) == 0.0

    with pytest.raises(ValueError):
        variance([])

    with pytest.raises(ValueError):
        variance([1])

def test_standard_deviation():
    """Test the standard deviation function."""
    assert standard_deviation([1, 2, 3, 4, 5]) == pytest.approx(1.58, rel=1e-2)
    assert standard_deviation([10, 20, 30]) == 10.0
    assert standard_deviation([1, 1, 1, 1]) == 0.0

    with pytest.raises(ValueError):
        standard_deviation([])

    with pytest.raises(ValueError):
        standard_deviation([1])
