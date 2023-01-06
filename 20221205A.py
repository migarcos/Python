# LISTAS

frutas = ['mango','pera','limón','piña']
mezcla = ['text1',8,'text2',76,54,'text3']
numbers = [23,45,56,76,37,92,81,18]

def menu():
    print('LISTAS DISPONIBLES\n[1]. frutas\n[2]. mezcla\n[3]. numbers')

def mostrarlista(nombre):
    for index in range(0,len(nombre)):
        print(index,':',nombre[index])






opc = 'y'
while opc == 'y':
    menu()
    lista = input('Presione el número de la lista a mostrar: ')
    if lista == '1':
        mostrarlista(frutas)
    elif lista == '2':
        mostrarlista(mezcla)
    elif lista == '3':
        mostrarlista(numbers)
    print()
    opc = input('¿desea continuar? [y] | [n]')
print('\nGracias por usar MARCsoft')
