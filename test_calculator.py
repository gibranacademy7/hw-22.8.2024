# from Terminal > pip install pytest
# from Terminal > pytest .
import pytest
import calculator

def test_calculator_add_small():
    # Arrange
    x: int = -1
    y: int = 0
    expected: int = -1

    # Act
    actual: int = calculator.add(x, y);

    # Assert
    assert actual == expected

def test_calculator_sub_small():
    x: int = 12
    y: int = 6
    expected: int = 6
    actual: int = calculator.subtract(x, y);
    assert actual == expected

def test_calculator_mul_small():
    x: int = 7
    y: int = 9
    expected: int = 63
    actual: int = calculator.multiply(x, y);
    assert actual == expected

def test_calculator_mul_zero():
    x: int = 99
    y: int = 0
    expected: int = 0
    actual: int = calculator.multiply(x, y);
    assert actual == expected

def test_calculator_div_small():
    x: int = 88
    y: int = 11
    expected: int = 8
    actual: int = calculator.divide(x, y);
    assert actual == expected

def test_calculator_div_zero_error_phase1():
    # test that we get an error when divide by zero
    x: int = 99
    y: int = 0
    try:
        actual: int = calculator.divide(x, y);
        assert False  # fail the test
    except ZeroDivisionError as e:
        assert True  # pass the test

def test_calculator_div_zero_error_phase2():
    x: int = 99
    y: int = 0
    with pytest.raises(ZeroDivisionError) as ex:
        actual: int = calculator.divide(x, y)

    assert str(ex.value) == "Cannot divide by zero!"

def test_calculator_power():
    x: int = 2
    y: int = 4
    exepected: int = 16
    actual: int = calculator.power(x, y);

    assert actual == exepected

def test_calculator_power():
    x: int = 3
    y: int = 2
    exepected: int = 9
    actual: int = calculator.power(x, y);

    assert actual == exepected

def test_calculator_power():
    x: int = 9
    y: int = 0
    exepected: int = 1
    actual: int = calculator.power(x, y);

    assert actual == exepected

def test_calculator_sqrt():
    x: int = 25
    expected: int = 5
    import math
    actual: int = calculator.sqrt(x);

    assert expected ==actual


def test_calculator_sqrt():
    import math
    x: int = -5

    with pytest.raises(ValueError) as e:
        actual: int = calculator.sqrt(x);

    assert str(e.value) == "math domain error"


def test_calculator_prime():
    x: int = 1
    expected: bool = False
    actual: bool = calculator.is_prime(x);

    assert expected == actual


def test_calculator_prime():
    x: int = 2
    expexted: bool = True
    actual: bool = calculator.is_prime(x);

    assert  actual == expexted


def test_calculator_prime():
    x: int = 16
    expected: bool = False
    actual: bool = calculator.is_prime(x);
    assert expected==actual


def test_calculator_prime():
    x: int = -3
    expected: bool = False
    actual: bool = calculator.is_prime(x)
    assert expected==actual


def test_calculator_prime():
    x: int = 0
    expected: bool = False
    actual: bool = calculator.is_prime(x);
    assert expected==actual


def test_calculator_factional():
    x: int = 4
    expected: int = 24
    actual: int = calculator.factorial(x);
    assert expected==actual


def test_calculator_factional():
    x: int = 0
    expected: int = 1
    actual: int = calculator.factorial(x);
    assert expected==actual


def test_calculator_factional():
    x: int = 1
    expected: int = 1
    actual: int = calculator.factorial(x);
    assert expected==actual


def test_calculator_factional():
    x: int = 5
    expected: int = 120
    actual: int = calculator.factorial(x);
    assert expected==actual

def test_calculator_factional():
    x: int = -3
    with pytest.raises(ValueError) as e:
        actual: int = calculator.factorial(x);

    assert str(e.value) == "Factorial not defined for negative values "