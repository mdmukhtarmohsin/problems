def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celcius_to_kelvin(celcius):
    return celcius + 273.15

def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

print(celcius_to_fahrenheit(100))
print(fahrenheit_to_celcius(212))
print(celcius_to_kelvin(100))
print(kelvin_to_celcius(373.15))