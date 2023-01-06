# Mostrar los números primos existentes del 1 al 100
'''
2 3 5 7 11 13 17 19 23 29 ... 97

hay 25 números primos del 1 al 100
'''
cont = 0
for i in range(1,101):
    for j in range(1,i+1):
        if i % j == 0:
            cont = cont + 1
    if cont == 2:
        print(i,end=' ')
    cont = 0

'''
for i in range(1,101):
    print(i,end=' ')

    - - - - - - 


cont = 0
for i in range(1,101):
    for j in range(1,i+1):
        if i % j == 0:
            cont = cont + 1
    if cont == 2:
        print(i,end=' ')
    cont = 0   

'''


