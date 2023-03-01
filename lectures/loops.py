# Session 0, lecture 2: loops
# IMPRS 2023, 01/03/2023

# Often, when working with data, we want the same operation to be repeated more than once
# We can do this using loops
# First, we will introduce the while-loop: it's very similar to an if-statement,
#  except that it will keep running the same block of code as long as the expression is True
# Compare that with the if-statement, which will only ever do something once
# This is an example that counts from 0 to 9
number = 0
while number < 10:
    print(number)
    number = number + 1

# For some practice, take a look at the following exercises:
# - countdown.py
# - repeat_password.py
# - guessing_game.py

# While loops are very useful, but their behaviour can sometimes be hard to predict:
# You don't know for sure how often something will happen at the start of the loop.
# In cases where you do know this, and you just want to loop over some collection of elements,
#  we can use a for-loop instead!

# A for-loop looks a bit different from a while-loop: you specify both some variable
#  that you use to loop over each value (here i), and the collection of things
#  you want to loop over (here range(10), which is a function that returns the
#  numbers from 0 to 9, like our while-loop above)
for i in range(10):
    print(i)

# We can loop over anything that can loosely be considered a collection of things;
#  for instance, a string is just a collection of letters!
for letter in 'Hello world':
    print(letter)

# If we want to define our own collections, we can define a list 
#  using the square brackets [] and commas to separate the values
numbers = [6, 4, 9, 13, 1]

# We can then loop over these like with any other collection:
for number in numbers:
    print(number)

# For some practice, take a look at the following exercises:
# - fizz_buzz.py
# - vowels.py
