# Exercise 2
# Temperature conversion: ask for a temperature in Celcius,
#  and then print the same temperature in Farenheit (multiply by 1.8 and add 32).

celcius = input('Give a temperature in Celcius: ')
celcius = float(celcius)
farenheit = 1.8 * celcius + 32
print(f'{celcius} degrees Celcius is {farenheit} degrees Farenheit')
