#!/usr/bin/env python3
"""
Autor : Patrick Ion <10758912@iespenyagolosa.com>
Fecha   : 31/10/22
Propósito: Calculo de areas
"""

print('Calculo de áreas - Elige una figura geométrica: ')
print('a) Triangulo')
print('b) Circulo')
Figura=input('Que figura quieres calcular (escribe T o C)?').upper()
if Figura=='T':
    base=float(input('Escribe la base: '))
    altura=float(input('Escribe la altura:'))
    area=base*altura/2
    print(f'Un triangulo de base {base} y altura {altura} tiene una área de {area}')
elif Figura=='C':
    radio=float(input('Escribe el radio: '))
    area=3.14*radio**2
    print(f'Un circulo de radio {radio} tiene un área de {area}')

