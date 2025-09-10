import pytest

def add(a, b):
    return a + b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

@pytest.mark.parametrize("a, b, expected", [
    (5, 7, 12),
    (-4, 0.5, -3.5),
    (0, 0, 0),
    (-2, -3, -5),
    (1.5, 2.5, 4.0)
])

def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (-10, 2, -5),
    (0, 10, 0),
    (10, 0, "Cannot divide by zero")
])

def test_divide(a, b, expected):
    assert divide(a, b) == expected
