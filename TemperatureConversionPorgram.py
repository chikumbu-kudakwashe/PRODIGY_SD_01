def celsius_to_fahrenheit(celsius: float) -> float: #converts celsius to fahrenheit
    return (celsius * (9/5)) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float: #converts fahrenheit to celsius
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius: float) -> float: #converts celsius to kelvins
    return celsius + 273.15

def kelvin_to_celsius(kelvin: float) -> float: #converts kelvins to celsius
    return kelvin - 273.15

def main():
    
    while True:
        '''
        prompts the user to enter the temperature
        if the temperature is not either an integer or a float, the user is prompted to enter the temperature until they get it right.
        '''
        try:
            temperature = float(input('Please enter the temperature: '))
            break
        except ValueError:
            print('Temperature not valid, try again')


    while True:

        '''
        prompts the user to enter the scale of measurement currently being used.
        if the scale is not in the provided scales of measurement, the user is prompted to enter the correct scale until they get it right.
        '''

        scale = input('Please enter the current scale of measurement: ').lower()
        if scale not in ('celsius', 'fahrenheit', 'kelvin'):
            print('Invalid scale of measurement, try again.')
        else:
            break

    if scale == 'celsius': 
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)

        print(f'\nFahrenheit: {fahrenheit:.2f}F\nKelvin: {kelvin:.2f}K')

    elif scale == 'fahrenheit':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = celsius_to_kelvin(celsius)

        print(f'\nCelsius: {celsius:.2f}C\nKelvin: {kelvin:.2f}K')
              
    else:
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = celsius_to_fahrenheit(celsius)

        print(f'\nCelsius: {celsius:.2f}C\nFahrenheit: {fahrenheit:.2f}F')


if __name__ == '__main__':
    main()
