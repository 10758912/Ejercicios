#!/usr/bin/env python3
"""
Autor : Patrick Ion <10758912@iespenyagolosa.com>
Fecha   : 09/11/22
Propósito: Calcular anchura y altura
"""

anchura=int(input('Dime la anchura del rectangulo : '))
altura=int(input('Dime la altura del rectangulo : '))

for i in range(altura):
    for j in range(anchura):
        print ('*', end=' ')
    print()


