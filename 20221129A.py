# determinar si un número es primo
usrnum = int(input('Dame un número: '))

contador = 0

for i in range(1,usrnum + 1 ):
    #print(usrnum,' % ',i,"= ",usrnum % i)
    #print(f'{usrnum} % {i} = {usrnum % i}')
    if usrnum % i == 0:
        contador = contador + 1

# print("\ncontador = ",contador)
if contador == 2:
    print(usrnum,' es primo ')
else:
    print(usrnum," no es primo")