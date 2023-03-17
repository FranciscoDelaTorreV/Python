import os
import time
import msvcrt
import numpy

#variables

total_A=0
total_B=0
total_C=0
total_D=0
lista_uwu=[1,2,3,4,5,6,7,8,9,10]
fila=''
columna=''
lista_comprador=[]
rut=''
res=''
letra=[10,9,8,7,6,5,4,3,2,1]
arreglo_persona=numpy.empty([3,100],object)


# def cantidad_depto():

#     if depto=='A':
#         contador_A=contador_A+1
#     elif depto=='B':
#         contador_B=contador_B+1
#     elif depto=='C':
#   	    contador_C=contador_C+1
#     elif depto=='D':
#         contador_D=contador_D+1
#def limpiar
def limpiar():
    print("CARGANDO...")
    time.sleep(2)
    os.system('cls')

#def mostrar disponibilidad
def mostrarDisponiblidad():
    print("      A    B    C    D")
    #letra.reverse()
    for x in range(10):
        if x==0:
            print(letra[x], end=' ')
        else:
            print(' '+str(letra[x]), end=' ')
        for y in range(4):
            if y==9:
                print(arreglo_depto[x,y]+'||', end=' | ')
            elif y==0:
                print('| |'+arreglo_depto[x,y], end='  | ')
            else:
                print(arreglo_depto[x,y], end='   |')
        print('')
    print('     ', end=' ')
    

#creación de mi arreglo
arreglo_depto=numpy.empty([11,4],dtype='object')
#lleno el arreglo
for columna in range(11):
    for fila in range(4):
        arreglo_depto[columna,fila]="✔️"

#limpiar
os.system('cls')

print('Bienvenido al hotel Murito')
while res!='7':
    print('1.Comprar departamento')
    print('2.Mostrar departamentos disponibles')
    print('3.Ver listado de compradores')
    print('4.Buscar comprador')
    print('5.Reasignar compra')
    print('6.Mostrar ganancias totales')
    print('7.Salir')
    res=input()
    if res in ('1','2','3','4','5','6','7'):
        if res=='1':
            print("Ingresa su rut")
            rut=input().replace('.','').replace('-','')

            lista_comprador.append(rut)
            for x in range(100):
                for y in range(3):
                    if arreglo_persona[y,x]==None:
                        arreglo_persona[y,x]=rut
                        arreglo_persona[y+1,x]=fila
                        arreglo_persona[y+2,x]=columna
                        lista_invert=arreglo_depto
            print("¿Cuantos departamento desea comprar?")
            cantidad_deptos=int(input())
            for x in range(cantidad_deptos):
                mostrarDisponiblidad()
                print("¿Qué depto desea?(Ejemplo: A3)")
                depto=input()
                # cantidad_depto()
               
                numero=['A','B','C','D']
                
                fila=depto[:1]
                fila=numero.index(fila.upper())
                
                columna=int(depto[1:])-1
                
                if arreglo_depto[columna,fila]=='✔️': 
                    print("DEPARTAMENTO DISPONIBLE\nCOMPRADO!")
                    arreglo_depto[columna, fila]='❌'

                else:
                    print("Depto OCUPADO")
        
        elif res=='2':
            mostrarDisponiblidad()
            print("Pulse una tecla para continuar")
            msvcrt.getch()

        elif res=='3':
            print('mostrando lista...')
            time.sleep(1.5)
            lista_comprador.sort()
            for elem in lista_comprador:
                print(elem)
            print('presione una tecla para continuar...')
            msvcrt.getch()
            limpiar()
   
        
        elif res=='4':
            print('introduzca el rut que desea buscar')
            buscar_rut=(input()).replace('.','').replace('-','')
            if buscar_rut in lista_comprador:
                print('RUT ENCONTRADO')
                time.sleep(1)
            else:
                print('RUT NO ENCONTRADO')
                time.sleep(1)
                
            print("PRESIONE UNA TECLA PARA CONTINUAR...")
            msvcrt.getch()
            os.system('cls')


        elif res=='5':
            print('reasignar comprador')
            buscar_rut=(input()).replace('.','').replace('-','')
            print(buscar_rut)
            print(lista_comprador)
            msvcrt.getch()
            if buscar_rut in lista_comprador:
                lista_comprador.remove(buscar_rut)
                print('RUT ELIMINADO')
                time.sleep(1)
                print('INGRESE NUEVO RUT')
                lista_comprador.append(input().replace('.','').replace('-',''))
            print('comprador reasignado con exito')
        

        elif res=='6':
           
            print('uwu')
        #    contador_total=contador_A+contador_B+contador_C+contador_D
 	    #     total_A=contador_A*3800
 		#      total_B=contador_B*3000
	    #     total_C=contador_C*2800
 		#      total_D=contador_D*3500
		#      total_apartamentos=total_A+total_B+total_C+total_D

        #    print('TIPO DE DEPARTAMENTO............CANTIDAD..........TOTAL................RECARGO POR PISO\n')
        #    print(f'    Tipo A                      {contadora_A}      {total_A}               X')
        #    print(f'    Tipo B                      {contador_B}       {total_B}               X')
        #    print(f'    Tipo C                      {contador_C}       {total_C}               X')
        #    print(f'    Tipo D                      {contador_D}       {total_D}               X\n')
        #    print(f'TOTAL...........................{contador_total}...{total_apartamentos}....X')  
        #    print("PRESIONE UNA TECLA PARA CONTINUAR...")
        #    msvcrt.getch()
        #    os.system('cls')
            
            

        else:
            print("GRACIAS POR PREFERIRNOS\nADIOS")
    else:
        #opción incorrecta del menú
        print("Opción incorrecta")
        limpiar()
