# Learning input and output Python use - Part II
# by Miguel Arcos - Apr 2022 - 

fst_Name = (input("First name: "))
last_Name = (input("Last name: "))
email = (input("Email address: "))
phone = input("Phone Number: ")
job = input("Job title: ")
id = input("ID Number: ")

hair_Color = input("What's your hair color? ")
eyes_Color = input("What's your eyes color? ")
start_Month = input("Month? ")
fsh_Training = input("yes / no : ")
tabs = '\t \t'
line = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
print(f'\nThe ID Card is:')
print(f'{line}')
print(f'{last_Name.upper()}, {fst_Name.title()}') #{tabs}
print(f'{job.title()}')
print(f'ID: {id}')
print(f'\n{email.lower()}')
print(f'Hair: {hair_Color.title()} {tabs} Eyes: {eyes_Color.title()}')
print(f'Month: {start_Month.title()} {tabs} Training: {fsh_Training.title()}')
print(f'{line}')


