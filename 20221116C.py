# ESTRUCTURAS DE CONTROL
# Condicionales anidados
''' Cree un programa que determine (dada la edad) 
si es     adulto,      joven,      niño  o  anciano (adulto mayor).
        >= 18  <60    >=12  <18     <12     >=60
'''
edad = int(input('Escriba su edad: '))

if edad >= 60:
    print('adulto mayor')
elif edad >= 18:
    print('adulto')
elif edad >= 12:
    print('joven')
else:
    print('niño')

print('---------')

if edad >= 60:
    print('adulto mayor')

if edad >= 18:
    print('adulto')

if edad >= 12:
    print('joven')

if edad < 12:
    print('niño')





