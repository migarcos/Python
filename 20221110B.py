# By Miguel Arcos - Nov 10 2022
# 
# Hallar la hipotenusa de un triángulo rectángulo

cateto1 = int(input(' Digite el valor del cateto adyacente: '))
cateto2 = int(input('Digite el valor cateto opuesto: '))

# calcular la hipotenusa
hipotenusa = (cateto1**2 + cateto2**2)**0.5

print(f' la hipotenusa es : {hipotenusa:.0f}')


