from app.calculator import Calculator

def test_multiplication():
    result = Calculator.multiplication(val1=2, val2=2)
    assert result == 4, "The multiplication function returns the wrong value"