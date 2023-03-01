# Exercise 3
# Ask for two numbers (use two separate input() calls),
#  and then print the relation between those numbers, e.g.
#  'x is larger than y', 'x is smaller than y', or 'x is equal to y'.
# Replace x and y with the actual numbers you entered.

x = int(input('Number 1: '))
y = int(input('Number 2: '))

if x > y:
    print(f'{x} is larger than {y}')
elif x < y:
    print(f'{x} is smaller than {y}')
else:
    print(f'{x} is equal to {y}')
