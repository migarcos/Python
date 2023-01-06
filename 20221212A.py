#lista = []
lista = ['Daniela','Cristian','Miguel','Mabel','David']

def menu():
    print('\nMAIN MENU\n1. Add\n2. Modify\n3. Remove\n4. Sort\n5. Show list elements')
    menuOption = input('Select an option using its number: ')
    return menuOption

def mostrar(nomLista):
    print()
    for i in range(0,len(nomLista)):
        print(f'{i}:{nomLista[i]}')

def agregar():
    dato = input('\n¿qué dato desea agregar? ')
    lista.append(dato)
    mostrar(lista)

def modificar():
    position = int(input('\n¿cuál es la position del elemento? '))
    lista[position] = input('\nescriba el nuevo dato: ')
    mostrar(lista)

def eliminar():
    mostrar(lista)
    dato = input('\n¿qué dato desea eliminar? ')
    lista.remove(dato)
    mostrar(lista)

def ordenar():
    lista.sort()
    mostrar(lista)

#Código principal
follow = 'y'
while follow.lower() == 'y':
    option = menu()
    
    if option == '1':
        agregar()
    elif option == '2':
        modificar()
    elif option == '3':
        eliminar()
    elif option == '4':
        ordenar()
    elif option == '5':
        mostrar(lista)
    

    follow = input('\nDo you want to continue? [y]|[n] ')


# 1. append() : adicionar elemento 
# 2. editar o modificar un elemento 
# 3. pop(index) remove() :borrar un elemento - Cristian
# 4. sort() :Cómo ordenar elemntos - Mabel


