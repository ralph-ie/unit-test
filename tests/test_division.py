"""Tests for the division function in the Calculator class."""

from app.calculator import Calculator

def test_division():
    """Divide two numbers"""
    result = Calculator.division(val1=5, val2=1)
    assert result == 5, "The division function returns the wrong value"
