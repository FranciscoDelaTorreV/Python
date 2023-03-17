import os
import time
os.system('cls')

acumulador=0

print('CUANTOS ALUMNOS TIENES?')
cantidad=int(input())

for thanos in range(1,cantidad+1):
    print(f'Ingrese la nota número {thanos}')
    nota=float(input())
    
    while nota>7 or nota<1:
        print('Nota inválida, vuelva a ingresar:')
        nota=float(input())
    acumulador=acumulador+nota
    promedio=acumulador/cantidad

print('CALCULANDO....')
time.sleep(5)    
print(f'El promedio del curso es {promedio}')
