import os
import time
import msvcrt
os.system('cls')
respuesta=0
rut=''
contrasena=''
contador_intentos=0
saldo=10000

while rut=='' or len(rut)<9:
    if contador_intentos==3:
        print("USUARIO BLOQUEADO")
        print("ACERQUESE A SU BANCO MAS CERCANO")
        time.sleep(3)
        break
    else:
        print("BIENVENIDO A BANCO DE TALCA")
        print("Ingrese su rut:")
        rut=input()
        print("Ingrese su contraseña:")
        contrasena=int(input())
        os.system('cls')
        contador_intentos=contador_intentos+1

    if (rut=='20123123-k' and contrasena==123) or (rut=='66666666-6' and contrasena==123):
        print("VALIDANDO DATOS")
        time.sleep(1)
        print("LOGIN CORRECTO")
        time.sleep(1)
        while respuesta!=5:
            print("BIENVENIDO AL SITIO WEB")
            print("1. Consultar saldo")
            print("2. Transferencia")
            print("3. Deposito de dinero")
            print("4. Planificar un giro")
            print("5. Cerrar sesión")
            respuesta=input()
            
            if respuesta=='1':
                print(f'Su saldo actual a la fecha es {saldo}')
                print('Presione cualquier tecla para continuar...')
                msvcrt.getch()
                os.system('cls')