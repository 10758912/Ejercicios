#!/usr/bin/env python3
"""
Autor : Patrick Ion <10758912@iespenyagolosa.com>
Fecha   : 07/11/22
Propósito: Calcular numeros consecutivos
"""

n=int(input("Dime un número: "))

if n>=0:
    for i in range (0,n+1):
        print(i,end=",")
else:
    for i in range(0,n-1,-1):
        print(i,end=",")

print()



