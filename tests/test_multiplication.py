"""Tests for the multiplication function in the Calculator class."""

from app.calculator import Calculator

def test_multiplication():
    """Multiply two numbers"""
    result = Calculator.multiplication(val1=5, val2=5)
    assert result == 25, "The multiplication function returns the wrong value"