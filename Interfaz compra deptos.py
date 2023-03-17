import os
import time
import msvcrt
import numpy

#variables
lista_uwu=['9','8','7','6','5','4','3','2','1','0']
lista_comprador=[]
contador_A=0
contador_B=0
contador_C=0
contador_D=0
res=''
letra=['10','9','8','7','6','5','4','3','2','1']
arreglo_persona=numpy.empty([3,100],object)
lista_rut=[]
#def suma depto
def suma_depto():
    if depto is 'A3' and 'A10':
        contador_A=contador_A+3800+100
    elif depto>="B3" and depto<='B10':
        contador_B=contador_B+100
    elif depto>="C3" and depto<="C10":
        contador_C=contador_C+100
    elif depto>="D3" and depto<="D10":
        contador_D=contador_D+100


#def limpiar
def limpiar():
    print("CARGANDO...")
    time.sleep(2)
    os.system('cls')

#def mostrar disponibilidad
def mostrarDisponiblidad():
    print("      A    B    C    D")
    for x in range(10):
        print(letra[x], end=' ')
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
            lista_comprador.append(int(input()))
            for x in range(100):
                for y in range(3):
                    if arreglo_persona[y,x]==None:
                        arreglo_persona[y,x]=lista_comprador
                        arreglo_persona[y+1,x]=fila
                        arreglo_persona[y+2,x]=columna
            print("¿Cuantos departamento desea comprar?")
            cantidad_deptos=int(input())
            for x in range(cantidad_deptos):
                mostrarDisponiblidad()
                print("¿Qué depto desea?(Ejemplo: 3B)")
                depto=input()
                suma_depto()
                numero=['A','B','C','D']
                lista_uwu.index(letra)
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
            buscar_rut=int(input())
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
            buscar_rut=int(input())
            if buscar_rut in lista_comprador:
                lista_comprador.remove(buscar_rut)
                print('RUT ELIMINADO')
                time.sleep(1)
                print('INGRESE NUEVO RUT')
                lista_comprador.append(int(input()))
            print('comprador reasignado con exito')
        

        elif res=='6':
            total_ganancias=contador_A + contador_B +contador_C + contador_D
            print(f'{total_ganancias}$')
            print("PRESIONE UNA TECLA PARA CONTINUAR...")
            msvcrt.getch()
            os.system('cls')
            
            

        else:
            print("GRACIAS POR PREFERIRNOS\nADIOS")
    else:
        #opción incorrecta del menú
        print("Opción incorrecta")
        limpiar()
