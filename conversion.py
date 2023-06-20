def celsius_to_fahrenheit(celsius):
    return celsius/5*9 + 32

def celsius_to_kelvin(celsius):
    return celsius+273.15
    
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin-273.15)


