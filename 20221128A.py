
char = input('Digite un caracter: ')
lineas = int(input('Escriba el # de líneas >3:  '))

i = 1
while i <= lineas:
    j = 1
    while j < i+1:
        print(char,end=' ')
        j = j + 1
    print('')
    i = i + 1

'''
for i in range(1,lineas+1):
    for j in range(1,i+1):
        print(char,end=' ')

* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
for i in range(lineas,0,-1):
    for j in range(1,i+1):
        print(char,end=' ')
    print('')


for i in range(lineas+1,1,-1):
    for j in range(1,i):
        print(char,end=' ')
    print('')

char = input('Digite un caracter: ')
lineas = int(input('Escriba el # de líneas >3:  '))

for i in range(1,lineas+1):
    for j in range(1,i+1):
        print(char,end=' ')
    print('')
'''