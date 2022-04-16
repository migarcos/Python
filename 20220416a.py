# Learning input and output Python use
# by Miguel Arcos - Apr 2022 

# simple form to use print and input
print("What's your name? ")
name = input()

# advance way to read and use the input
color = input("What's your favorite color? ")

# obtain year 'str' and change to int
yr =  int(input("What year were you born? "))

# using a python library 
from datetime import date
actualDay = date.today()

print('\n' + color +' is a beatiful color '+ name)
# you can only concatenate str values
print('Wow! You are ', end='') 
#  int(actualDay.year) - yr, obtain client age to the current year
# More info to this on https://www.geeksforgeeks.org/python-program-to-print-current-year-month-and-day/
print(int(actualDay.year) - yr, end='')  
print(' years old')

""" a multiline text 
 can work as a large comment
 if isn't assigned """