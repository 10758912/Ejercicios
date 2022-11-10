año=int(input('Introduce un año para comprobar si es bisiesto:'))
condicion1= (año % 4==0) and not (año % 100 == 0)
condicion2=año % 400 == 0

if condicion1 or condicion2:
    print(f' {año} es un año bisiesto.')
else:
    print(f'{año} no es un año bisiesto.')
