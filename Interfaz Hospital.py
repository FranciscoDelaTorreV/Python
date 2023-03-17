import time
import os 
import numpy
import msvcrt

os.system('cls')

#variables owo

resp=''

#Listas
 
lista_paciente_rut=[]

#limpiar pantalla

def limp():
    print("ESPERE UN SEGUNDO...")
    time.sleep(3)
    os.system('cls')

print('NOMBRE DEL OPERARIO')
nombre_trabajador=input()
limp()


#MENU URGENCIA

while resp!='6':
    print('SERVICIO DE URGENCIAS DUOC UC\n')
    print('     MENÚ DE URGENCIAS   ')
    print('1. INGRESAR FICHA PACIENTE')
    print('2. BUSCAR FICHA POR RUT DEL PACIENTE')
    print('3. BUSCAR MEDICAMENTOS POR RUT DEL PACIENTE')
    print('4. ELIMINAR FICHA DE UN PACIENTE')
    print('5. VER LISTA DE PACIENTES ATENDIDOS')
    print('6. SALIR')
    resp=input()
    limp()

#DESAROLLO OPCION 1

    if resp=='1':
        print('INGRESE LOS DATOS DEL PACIENTE\n')
        print('INGRESAR RUT DEL PACIENTE(EJ: 11.123.456-7)')
        lista_paciente_rut.append(input())#VALIDACION DE RUT
        os.system('cls')            
        print('NOMBRES DEL PACIENTE(EJ: FRANCISCO ESTEBAN)')
        nombre_paciente=input()
        os.system('cls')
        print('INGRESAR APELLIDOS DEL PACIENTE(EJ: GONZALEZ TAPIA)')
        apellido_paciente=input()
        os.system('cls')
        print('SEXO DEL PACIENTE (M-F)')
        sexo=input()
        os.system('cls')
        print('NIVEL URGENCIA DE ATENCION (EJ: GRAVE-MODERADO-LEVE)')
        nivel_urgencia=input()
        os.system('cls')
        print('ESTADO CIVIL PACIENTE')
        estado_civil=input()
        os.system('cls')
        print('EDAD PACIENTE(AÑOS)')
        edad_paciente=input()
        os.system('cls')
        print('TELEFONO CELULAR (EJ: 9 66666665')
        telefono_movil=input()
        os.system('cls')
        print('DOMICILIO(EJ: LOS LIRIOS 1265)')
        domicilio_paciente=input()
        os.system('cls')
        print('HORA ATENCIÓN (EJ: 15:30)')
        hora_atencion=input()
        limp()

#DESAROLLO OPCION 2

    elif resp=='2':
        print('INTRODUZCA EL RUT A BUSCAR:')
        buscador=input()#VALIDACION DE RUT
        if(buscador in lista_paciente_rut):
            print("RUT ENCONTRADO")
            print('IMPRIMIENDO DATOS...')
            time.sleep(2)
            print(f'NOMBRES:.................{nombre_paciente}')
            print(f'APELLIDOS:...............{apellido_paciente}')
            print(f'NIVEL DE URGENCIA:.......{nivel_urgencia}')
            print(f'SEXO:....................{sexo}')
            print(f'ESTADO CIVIL:............{estado_civil}')
            print(f'EDAD:....................{edad_paciente}')
            print(f'TELEFONO MOVIL:..........{telefono_movil}')
            print(f'DOMICILIO:...............{domicilio_paciente}')
            print(f'HORA ATENCION:...........{hora_atencion}')
            
            print('PRESIONA CUALQUIER TECLA PARA CONTINUAR...')
            msvcrt.getch()
            os.system('cls')
        else:
            print('RUT NO ENCONTRADO, INTENTE NUEVAMENTE')

#DESAROLLO OPCION 3

    elif resp=='3':
        print('LISTA DE POSIBLES MEDICAMENTOS\n')
        print('1. PARACETAMOL')
        print('2. KETOPROFENO')
        print('3. KETOROLACO')
        print('4. CLORFENAMINA')
        print('5. IBUPROFENO')
        time.sleep(2)
        print('INGRESE RUT DE PACIENTE A BUSCAR MEDICAMENTOS')
        buscar_medicamento=input()#VERIFICADOR DE RUT
        if (buscar_medicamento in lista_paciente_rut):
            print('RUT ENCONTRADO')
            print('IMPRIMIENDO LISTA DE MEDICAMENTOS..')
            time.sleep(2)

        else:
            print('RUT NO ENCONTRADO, INTENTE NUEVAMENTE')

#DESAROLLO OPCION 4

    elif resp=='4':
        print('INGRESE RUT DE PACIENTE A ELIMINAR')
        buscar_paciente=input()#VERIFICADOR DE RUT
        if buscar_paciente in lista_paciente_rut:
            lista_paciente_rut.remove(buscar_paciente)
            print('ELIMINANDO RUT DEL SISTEMA, UN SEGUNDO POR FAVOR....')
            time.sleep(2)
            print('FICHA DE PACIENTE ELIMINADA EXITOSAMENTE')
        else:
            print('RUT DE PACIENTE INEXISTENTE')
            print('INTENTE DE NUEVO')    

#DESAROLLO OPCION 5

    elif resp=='5':
        print('LISTADO DE PACIENTES SERVICIO URGENCIA DUOC UC\n')
        print('IMPRIMIENDO LISTA DE PACIENTES....')
        time.sleep(2)
        listado_pacientes_arreglo=sorted(lista_paciente_rut)
        arreglo_bidimensional=numpy.array(listado_pacientes_arreglo)
        for i in range(len(arreglo_bidimensional)):
            print(arreglo_bidimensional[i])
        print("PRESIONE UNA TECLA PARA CONTINUAR...")
        msvcrt.getch()
        os.system('cls')

#DESAROLLO OPCION 6        

    elif resp=='6':
        print('GRACIAS POR PREFERIR SERVICIO DE URGENCIAS DUOC UC')
        print('QUE TENGA UN BUEN DIA')
        time.sleep(3)
        break

#DESAROLLO ELSE

    else:
        print('OPCION INVALIDA, INTENTE NUEVAMENTE')                     