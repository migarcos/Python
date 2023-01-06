# ESTRUCTURAS DE CONTROL
# Condicionales anidados

# Nota 0-5  Ganó Perdió ó habilita
# 4 o 5 ganó   3 habilita   0,1,2  perdió

grade = int(input('deme la nota'))

if grade > 3: 
    print('ganó')
else:
    if grade < 3: 
        print('perdió')
    else:
        print('habilita')


if grade > 3: 
    print('ganó')
elif grade < 3: 
    print('perdió')
else:
    print('habilita')
