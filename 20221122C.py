# ESTRUCTURAS DE CONTROL
# CICLOS O LOOPS -  CICLO FOR

# muestre los n (solicitar el num) 1ºs múltiplos del x
# x -> se debe pedir al usuario

num = int(input('Digite su número: ')) # x
multiplos = int(input('¿Cuántos múlt desea?: ')) # n

for i in range(1,multiplos+1):
    print(i*num,end=' ')

print('\n - - - - - - - - - ')

sup = multiplos * num 

for i in range(num,sup+1,num):
    print(i,end=' ')