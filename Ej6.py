#!/usr/bin/env python3
"""
Autor : Patrick Ion <10758912@iespenyagolosa.com>
Fecha   : 26/10/22
Propósito: Coeficientes de equaciones de segundo grado
"""

print('Coeficientes de equaciones de segundo grado') 
a=float(input('Escribe valor de a:'))
b=float(input('Escribe valor de b:'))
c=float(input('Escribe valor de c:'))
x1=int(-b+(b**2-4*a*c)**(1/2))/(2*a)
x2=int(-b-(b**2-4*a*c)**(1/2))/(2*a)
print(f'Las soluciones de la equación son {x1} y {x2} ')



