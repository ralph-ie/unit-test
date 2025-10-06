"""Tests for the subtraction function in the Calculator class."""

from app.calculator import Calculator

def test_subtraction():
    """Subtract two numbers."""
    result = Calculator.subtraction(val1=3, val2=2)
    assert result == 1, "The subtraction function returns the wrong value"
