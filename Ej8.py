#!/usr/bin/env python3
"""
Autor : Patrick Ion <10758912@iespenyagolosa.com>
Fecha   : 08/11/22
Propósito: Calcular numeros consecutivos
"""

numero=int(input("Dime un número positivo: "))

while numero<=0:
    print('Te he pedido un número positivo!!')
    numero=int(input('Dime un número positivo:'))

for i in range(0,numero+1):
    print(i,end=',')

print()
for i in range(numero,0-1,-1):
    print(i,end=',')

print()
for i in range(1,numero):
    print(i,end=',')

print()
for i in range(numero-1,0,-1):
    print(i,end=',')

print()
for i in range(0,numero+1,numero,0-1):
 for i in range(numero,0-1):
    print(i,end=',')
