# Exercise 6
# Part 1
# The code below picks a random number between 1 and 10.
# Extend this code so that it will keep asking the user for guesses,
#  until they have guessed the correct number.
# Give feedback on whether the number is correct or incorrect.
# If you accidentally get stuck in a loop, you can just close the terminal
#  you are using to stop running it.

from random import randint

number = randint(1, 10)  # Generates a number between 1 and 10
guess = int(input('Guess the number: '))

while guess != number:
    guess = int(input('Incorrect! Try again: '))

print('Correct!')


# Part 2
# When you have done this, take a look at your solution to comparison.py;
# Can you extend this guessing game so that it uses a number between 1 and 100,
#  and gives feedback to the user whether the guessed number is higher or lower
#  than the actual number?

from random import randint

number = randint(1, 100)  # Generates a number between 1 and 100
guess = int(input('Guess the number: '))

while guess != number:
    if guess > number:
        print('Incorrect, lower!')
    else:
        print('Incorrect, higher!')
    
    guess = int(input('Try again: '))

print('Correct!')
