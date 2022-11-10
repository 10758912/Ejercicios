#!/usr/bin/env python3
"""
Autor : Patrick Ion <10758912@iespenyagolosa.com>
Fecha   : 09/11/22
Propósito: Calcular valores
"""

valor_i=int(input('Dime el valor inicial: '))
valor_f=int(input('Dime el valor final: '))

while valor_i>valor_f:
    print('El valor final no es mayor que el valor inicial')
    valor_f=int(input('Dime el valor final'))

for i in range(valor_i, valor_f+1):
    if i%2==0:
        print(i,end=',')
print()