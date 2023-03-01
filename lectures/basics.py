# Session 0, lecture 1: Python basics
# IMPRS 2023, 01/03/2023

# You can use the print() function to print some value
# A function is simply some code that someone else wrote, that you're calling
# You may provide arguments in between the parentheses, and the function may return some value
# Print, for instance, takes whatever you want it to print as an argument, and returns nothing
print('Hello world!')

# You can use variables to store values, and use them anywhere where you can also use a value:
text = 'Hello world!'
print(text)

# The len() function takes a string, and returns the length of a string (of text)
# We assign the output of len() to a variable here, and then print that
length = len('Hello world!')
print(length)

# The input() function asks the user for input, and returns that input as a string
name = input('What is your name?')
print(name)

# We can concatenate strings using the + operator
print('Hello ' + name)

# We can use methods to do something to a particular object
# Methods are very similar to functions, but they always apply to some object
# You call a method by specifying the object first, followed by a dot (.),
#  and then the method name, with parentheses which (optionally) contain the arguments
# Passing arguments and returning values works in the same way as with functions
# Here, we use the .upper() method to convert a string to upper-case letters
print('Hello ' + name.upper())

# Besides strings, there are also numbers
whole_number = 5  # Integer
floating_point = 3.14  # Floating point number

# You can use +, -, *, /, ** to do calculations with those numbers
print(whole_number ** 2)

# We cannot add numbers to strings, so the line below would give an error
# print('The number is ' + whole_number)
# Instead, we need to first convert the number to a string, using the str() function
print('The number is ' + str(whole_number))  

# You can also use the int() and float() functions to convert 
#  strings to integers and floating point numbers, respectively

# Another way of formatting strings containing other variables / values,
#  is using f-strings, which will automatically convert anything in between
#  the curly braces {} to a string:
text = f'Hello {name}, the number is {whole_number}'
print(text)

# One final type of value is the boolean, which can be either True or False
# On its own, it is not very useful, but it can be used for logic =,
#  and it's what you get when you perform comparisons.
# For instance, you can compare strings using == (equals) and != (does not equal),
#  and numbers using those and additionally <, <=, >, and >=
my_boolean = whole_number >= 5  # Is whole_number larger than or equal to five?
print(my_boolean)

# We can use booleans in if-statements to conditionally evaluate code, like so:
whole_number = 1
if whole_number > 10:
    print('That is a large number')
else:
    print('That is a small number')

# For some practice, take a look at the following exercises:
# - password.py
# - temperature.py
# - comparison.py
