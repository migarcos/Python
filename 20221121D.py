# repetir hasta que el usuario idga que no
# mostrar los 10 1ºs múltiplos 
# de un nùmero solicitado al usuario
num = int(input('Escriba su número: '))

k = 0

while k < 10:
    k = k + 1
    print(f'{num} * {k:2} = {num * k:3}')
    

print('hemos terminado')
