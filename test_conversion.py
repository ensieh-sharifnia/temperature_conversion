from conversion import celsius_to_fahrenheit
import pytest
def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(10) == 50

def test_celsius_to_fahrenheit_invalid():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("str")

def test_celsius_to_fahrenheit_none():
    assert celsius_to_fahrenheit(None) is None