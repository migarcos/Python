# Learning input and output Python use
# by Miguel Arcos - Apr 2022 

# simple form to use print and input
print("What's your name? ")
name = input()

# advance way to read and use the input
color = input("What's your favorite color? ")

# obtain year 'str' and change to int
yr =  int(input("What year were you born? "))

start = '\033[1m'
end = '\033[0m'
#read it https://stackoverflow.com/questions/12492810/python-how-can-i-make-the-ansi-escape-codes-to-work-also-in-windows
# https://bugs.python.org/issue29059

# people say that ANSI codes works to show text bold formatted, but it doesn't work on Windows
print('\n' + start + color + end + ' is a beatiful color ' + start + name + end)

# I try to bold text using f-strings but doesn't work
# print(f'\n \033[1m{color}\033[0m is a beautiful color \033[1m{name.capitalize()}\033[0m')

'''
# you can only concatenate str values
print('Wow! You are ', end='')
#  int(actualDay.year) - yr, obtain client age to the current year
# More info to this on https://www.geeksforgeeks.org/python-program-to-print-current-year-month-and-day/
print(int(actualDay.year) - yr, end='')  
print(' years old') 
'''
# obtain year 'str' and change to int
yr =  int(input("What year were you born? "))

# using a python library 
from datetime import date
actualDay = date.today()

# I'm using f-strings (formatted string literals) on the next line
print(f"Wow! you are {int(actualDay.year) - yr} years old")
# To learn more about that... https://realpython.com/python-f-strings/


""" a multiline text 
 can work as a large comment
 if isn't assigned 
 
 class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


 """