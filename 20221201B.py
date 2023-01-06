#CREAR UN PROGRAMA CON MENU
def menu():
    print('1. Determinar primo\n2. Mostrar n primos \n3. Mostrar #s primos en un rango')
# definir funciones 
def primo():
    number = int(input('Give me your number: '))
    cont = 0
    for k in range(1,number+1):
        if number % k == 0:
            cont = cont + 1
    if cont == 2:
        print('El número es PRIMO')
    else:
        print('El número no es PRIMO')
def nprimos():
    cuantos = int(input('Cuántos quiere? '))

# CODIGO PRINCIPAL
menu()
opc = input('escriba su opción ')

if opc == '1':
    primo() #debe definir la función, ver linea 5
elif opc == '2':
    nprimos()  #debe definir la función, ver ínea 15
elif opc == '3':
    rangoprimos()  #debe definir la función
else:
    print('opción invalida')