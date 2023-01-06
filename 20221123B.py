# Crear un ciclo que permita hallar 
# el àrea de un triángulo ó de un círculo 
# según desee el usuario y 
# hasta que diga que no quiere continuar

def areaT(): # definir una función
    b = int(input('Digite la base: '))
    h = int(input('Digite la altura: '))
    print('El área del triángulo es ', b*h/2)

def areaC():
    radio = int(input('Digite el radio: '))
    print('El área del círculo es: ', 3.1416 * radio**2)

continuar = 'si'

while continuar != 'no' and continuar != 'NO':
    opc = input("\n[1]. Área Triángulo\n[2]. Área del Círculo")
    if opc == '1':
        areaT()
    elif opc == '2':
        areaC()

    continuar = input('\n¿Quiere continuar?  "si" / Terminar "no" ')

print('\n* hemos terminado *')

''' 
continuar = 'si'

while continuar == 'si' or continuar == 'SI':
    print('\nestamos en un ciclo')

    continuar = input('\n¿Quiere continuar?  "si" / Terminar "no" ')

print('\n* hemos terminado *')
'''
