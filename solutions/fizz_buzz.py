# Exercise 7
# Print the numbers from 0 to 99 using a for-loop, 
#  but every time a number is a multiple of 3
#  you print 'Fizz' instead of the number, every
#  time it is a multiple of 5 you print 'Buzz',
#  and when a number is a multiple of both, you print 'FizzBuzz'.

# Checking divisibility:
# You can use the % operator on two numbers to calculate the remainder;
#  when a remainder is 0, that means the number on the left
#  is divisible by the number on the right; e.g.: 
#    x % 2 == 0
#  equals True when x is divisible by 2 (i.e. even), and False otherwise

# Combining different boolean comparisons
# You can combine different boolean expressions using 'and' and 'or', e.g.:
#    x > 1 and x < 6
#  only returns true when x is between 2 and 5

for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
