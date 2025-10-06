from app.calculator import Calculator

def test_division():
    result = Calculator.division(val1=4, val2=1)
    assert result == 4, "The division function returns the wrong value"
