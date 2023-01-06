# hallar área de un triángulo por semiperimetro

lado1 = input('Deme un lado1: ')
lado2 = input('Deme un lado2: ')
lado3 = input('Deme un lado3: ')

# voy a realizar una asignación (PROCESO)
perimetro = int(lado1)+int(lado2)+int(lado3)
# calculo el semiperimetro
s = perimetro / 2

print(f'El perimetro es {perimetro}')

# calculo el área por semiperimetro
As = (s*(s-int(lado1))*(s-int(lado2))*(s-int(lado3)))**0.5

print(f'El Área por semiperimetro es {As}')


