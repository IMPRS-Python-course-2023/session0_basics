# Exercise 8
# Ask the user to input some text, and use a for-loop
#  to count the number of vowels in that text.
# Make sure to count both upper- and lower-case letters!
# You can check whether a letter is in a longer list
#  of letters using the 'in' keyword, e.g.:
#    'z' in 'xyz'
#  returns True, whereas
#    'a' in 'xyz'
#  returns False.

text = input('Please provide some text: ')

vowels = 0
for letter in text.lower():
    if letter in 'aeoui':  # plus maybe y
        vowels = vowels + 1

print(f'There are {vowels} vowels in your text!')
