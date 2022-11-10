#!/usr/bin/env python3
"""
Autor : Patrick Ion <10758912@iespenyagolosa.com>
Fecha   : 09/11/22
Propósito: Calcular anchura y altura
"""

frase='Tengo una hormiga en la barriga'
vocal=input('Dime una vocal: ')
VOCALES='aeiou'
frase_nueva=[]

for i in range(len(frase)):
    if frase [i] in VOCALES:
        frase_nueva.append(vocal)
    else:
        frase_nueva.append(frase[i])

print (f'La frase es ahora: {frase_nueva}')


