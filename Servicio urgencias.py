import time
import sys
from intertools import cycle
import os

os.system('cls')

contador_mujer='0'
contador_hombre='0'
contador_i='0'
contador_pacinete_con_reposo='0'
edaad=''
numero=''
rut=''
resp_menu=''
resp_mto=0
def edad_paciente(edad):
    if edad<0 and edad>120:
        print('ERROR, DEBE INGRESAR UNA EDAD QUE ESTÉ ENTRE LOS 0 Y 120 AÑOS. VUELVA A INENTAR')
        edaad=int(input())

def validarRut(rut):
	rut = rut.upper()
	rut = rut.replace("-","")
	rut = rut.replace(".","")
	aux = rut[:-1]
	dv = rut[-1:]
	revertido = map(int, reversed(str(aux)))
	factors = cycle(range(2,8))
	s = sum(d * f for d, f in zip(revertido,factors))
	res = (-s)%11
	if str(res) == dv:
		return True
	elif dv=="K" and res==10:
		return True
	else:
		return False
def main():
	print(validarRut(sys.argv[1] ))
if __name__=="__main__":
	main()

while resp_menu!='6':
    print('Servicio de urgencias')
    print('---------------------')
    print('1. Ingresar ficha del paciente')
    print('2. Buscar ficha por rut')
    print('3. Buscar medicamentos por rut')
    print('4. Eliminar ficha del paciente')
    print('5. Listar pacientes atendidos')
    print('6. Salir')
    resp_menu=input()
    if resp_menu in ('1','2','3','4','5'):
        if resp_menu=='1':
            print('Ingrese fecha de atención')
            fecha=int(input())
            print('Ingrese hora de atención')
            hora=float(input())
            print('ingrese nombre y apellido del personal')
            nom=input()
            print('---------------------------------------')
            print('IDENTIFICACIÓN PACIENTE')
            print('-----------------------------')
            print('Ingrese el nivel de urgencia')
            print('1. Riesgo vital')
            print('2. Muy urgente(10 mins espera)')
            print('3. Urgente (60 mins espera)')
            print('4. Normal (120 mins espera')
            nu=int(input())
            print('Ingrse nombre y apellido del paciente')
            nom=input()
            print('Ingrese RUT del paciente')
            rut=input()
            #validacion del rut
            validarRut()
            main()
            print('Ingrese estado civil')
            e_c=input()
            print('Ingese domicilio')
            domi=float(input())
            print('Ingrese número de telefono')
            numero=float(input())
            ##validar el sexo 
            print("Ingrese sexo del pciente (F-M-I):")
            sexo=input()
            while sexo!='F' and sexo!='M' and sexo!='I':
                print("Error, ingrese sexo nuevamente(F-M-I):")
                sexo=input()
                if sexo==M:
                    contador_hombre=contador_hombre+1
                elif sexo==F:
                    contador_mujer=contador_mujer+1
                elif sexo==I:
                    contador_i=contador_i+1

            ## validar la edad
            print('Ingrese edad del paciente')
            edad=int(input())
            edad_paciente(edad)
            print('Ingrese grupo sanguineo del paciente')
            sangre=input()
            print('Ingrese el diagnostico del paciente')
            diagnostico=input()
            #aqui ingresa los medicamentos
            print('Ingrese la cantidad de medicamentos')
            cantidad=int(input())
            while resp_mto!='5':
                print('Lista de medicamentos')
                print('1. Paracetamol ')
                print('2. Lidocaína')
                print('3. Omeprazol')
                print('4. Penicilina')
                print('5. Salbutamol')
                print('6. Salir')
                resp_mto=int(input())
                ##validacion del menú
                if resp_mto in ('1','2','3','4','5'):
                    if resp_mto=='1':
                        print('Medicamento registrado con exito')
                    elif resp_mto=='2':
                        print('Medicamento registrado con exito')
                    elif resp_mto=='3':
                        print('Medicamento registrado con exito')
                    elif resp_mto=='4':
                        print('Medicamento registrado con exito')
                    elif resp_mto=='5':
                        print('Medicamento registrado con exito')                

                else:
                    print('Opcion invalida')    

            ##validar el si y el no
                print('¿El paciente asiste acompañado? (ponga Si o No)')
                compañia=input().upper
                if compañia='SI':
                    contador_pacinete_con_reposo=contador_pacinete_con_reposo+1
                time.sleep(3)
                os.system('cls')