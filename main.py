# 1 - Create a program that asks the user to enter their name and their age. Print out a message addressed
#  to them that tells them the year that they will turn 100 years old.

# Request input from user
name = str(input('Enter your name: '))
age = int(input('Enter your age in years: '))


# Request an additional number and print output this number of times
number = int(input('Please enter an additional number: '))

# Evaluate input
year = (100 - age) + 2017

# Output
print(('Dear Mr/Ms ' + name + ', you will turn 100 years old on ' + str(year) + '\n') * number)