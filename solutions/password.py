# Exercise 1
# Ask for a 'password' and ensure that it is at least 8 characters long,
#  using the len() function.
# Then ask for the user to type the password again, and check that it
#  is the same. 
# Print output indicating whether the password is long enough and
#  whether it was repeated correctly.

password = input('Please type a password: ')
length = len(password)

if length >= 8:
    print('Password long enough')
    repeat_password = input('Please repeat your password: ')
    if password == repeat_password:
        print('Correct!')
    else:
        print('Passwords do not match')
else:
    print('Password too short!')
