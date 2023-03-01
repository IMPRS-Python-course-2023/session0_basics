# Exercise 5
# Ask for a 'password' and ensure that it is at least 8 characters long;
#  use a while-loop to keep asking until the password is long enough.
# Then ask for the user to type the password again, and check that it
#  is the same; while it is not the same, keep asking again.
# Take a look at your solution to password.py to get started!

password = input('Please type a password: ')

while len(password) < 8:
    password = input('Too short! Please pick again: ')

print('Password long enough')

repeat_password = input('Please repeat your password: ')
while password != repeat_password:
    repeat_password = input('Incorrect! Type again: ')

print('Correct!')
