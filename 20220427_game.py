# Create a fun paragraph asking for words
# April 2022

one = input('adjetive: ')
two = input('animal: ')
three = input('verb: ')
four = input('exclamation: ')
five = input('verb: ')
six = input('verb: ')

seven = input('profession:')
seven_New = seven.lower()
if seven_New[0] in ('a','e','i','o','u'):
   seven_New = 'An ' + seven_New
else:
   seven_New = 'A ' + seven_New
eight = input('verb')

print('\nYour story is:')
print(f'\n The other day, I was really in trouble. It all started when I saw a very {one.lower()} {two.lower()} {three.lower()} down the hallway. "{four.title()}!" I yelled. But all I could think to do was to {five.lower()} over and over. Miraculously, that caused it to stop, but not before it tried to {six.lower()} right in front of my family. {seven_New} that {eight.lower()} near there began to laugh.')

