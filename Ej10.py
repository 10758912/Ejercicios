#!/usr/bin/env python3
"""
Autor : Patrick Ion <10758912@iespenyagolosa.com>
Fecha   : 09/11/22
Propósito: Calcular ffactorial
"""

numero=int(input("Dime un número : "))
factorial=1

for i in range(1,numero+1):
    factorial=factorial*i

print(f'El factorial de {numero} es {factorial}')



