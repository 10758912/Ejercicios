#!/usr/bin/env python3
"""
Autor : Patrick Ion <10758912@iespenyagolosa.com>
Fecha   : 09/11/22
Propósito: Calcular numeros
"""

numeros=int(input("¿Cuantos valores vas a introducir? : "))
minimo=1000000000000000
maximo=0
suma=0
media=0
for i in range(1, numeros+1):
    num=int(input(f'Dime el numero {i}: '))
    suma += num
    if num < minimo:
        minimo = num
    if num > maximo:
        maximo = num
media = suma / numeros
print(f'La suma de los {numeros} numeros es {suma}')
print(f'El numero mas pequeños de los introducidos es: {minimo}')
print(f'El numero mas grande de los introducidos es: {maximo}')
print(f'La media de los numeros introducidos es: {media}')