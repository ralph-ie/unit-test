from app.calculator import Calculator

def test_subtraction():
    result = Calculator.subtraction(val1=10, val2=5)
    assert result == 5, "The subtraction function returns the wrong value"
