"""This is the starting test file"""

from app.calculator import Calculator

def test_addition():
    """Add two numbers"""
    result = Calculator.addition(val1=3, val2=4)
    assert result == 7, "The addition function returns the wrong value"
