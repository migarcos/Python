# Mostrar los 100 primeros números primos

cont = 0 #cuenta nos primos
i = 2 # expone un número

while cont < 100:
    primo = 0 # identifica primo
    for j in range(1, i+1):
        if i % j == 0:
            primo = primo + 1
    if primo == 2:
        cont = cont + 1
        print(cont,'->',i)

    i = i + 1


# 1ero mostrar los números hasta un valor 
# determinado por una bandera 
'''
cont = 0

while cont < 100:

    cont = cont + 1

print(cont)
'''