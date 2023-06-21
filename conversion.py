def celsius_to_fahrenheit(celsius):
    """convert celsius to fahrenheit

    Args:
        celsius (float): temperature in celsius

    Returns:
        float: temprature in fahrenheit
    """
    return celsius/5*9 + 32

def celsius_to_kelvin(celsius):
    """convert celsius to kelvin

    Args:
        celsius (float): temperature in celsius

    Returns:
        float: temprature in kelvin
    """
    return celsius + 273.15
    
def kelvin_to_celsius(kelvin):
    """convert kelvin to celsius

    Args:
        kelvin (float): temperature in kelvin

    Returns:
        float: temperature in celsius
    """
    return kelvin - 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

def check_unit_validity(unit):
    if unit in ['F', 'K', 'C']:
        return True
    else:
        return False
def check_temperature_validity(temperature, unit):
    abs_zero = {'F': -459.67,
                'C': -273.15,
                'K': 0}
    if temperature < abs_zero[unit]:
        return False
    else:
        return True

def convert_temperature(temperature, unit):
    if not check_unit_validity(unit):
        return "Invalid unit"
    if not check_temperature_validity(temperature, unit):
        return "Invalid temperature"
    if unit == "F":
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = celsius_to_kelvin(celsius)
        return celsius, kelvin
    elif unit == "C":
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        return fahrenheit, kelvin
    elif unit == "K":
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return celsius, fahrenheit
    
if __name__ == '__main__':
    print(convert_temperature(0, 'F'))
    print(convert_temperature(0, 'C'))
    print(convert_temperature(0, 'K'))
    print(convert_temperature(-700, 'K'))
    print(convert_temperature(-800, 'C'))
    print(convert_temperature(-900, 'F'))
    print(convert_temperature(-400, 'k'))


