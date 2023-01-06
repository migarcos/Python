# ESTRUCTURAS DE CONTROL
# CICLOS O LOOPS -  CICLO FOR

# muestre los n (solicitar el num) 1ºs múltiplos del 13

#num = int(input('Digite su número: '))
multiplos = int(input('¿Cuántos múlt desea?: '))

sup = multiplos * 13 # 65

for i in range(13,sup+1,13):
    print(i)

print(' - - - - - - - ')

for i in range(1,multiplos+1):
    print(i*13)
