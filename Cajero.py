import os
import time
import msvcrt
os.system ('cls')
contraseña = '1234'
largo_contraseña = len (contraseña)
rut = '11111111-1'
largo_rut = len (rut)
intento = 0
saldo = 155000
deposito = 0
saldo_cajero = 350000
comprobante = ''



print ('BIENVENIDO')
print ('')
print ('INSERTE SU TARJETA')
time.sleep (4)
print ('VERIFICANDO...')
time.sleep (3)
os.system ('cls')
print ('INGRESE CONTRASEÑA DE 4 DIGITOS')
contraseña = input ()
time.sleep (1)
os.system ('cls')
print ('CONECTANDO...')
time.sleep (3)
os.system ('cls')

while contraseña != '1234':
    largo_contraseña = len (contraseña)
    
    while largo_contraseña > 4 or largo_contraseña < 4  or largo_contraseña == '':
        
        print ('NO INGRESES MAS NI MENOS DE 4 NUMEROS O CARACTERES INCORRECTOS')
        print ('VUELVE A INTENTAR')
        contraseña = input ()
        largo_contraseña = len (contraseña)
        time.sleep (2)
        os.system ('cls')

        if contraseña == '1234' or largo_contraseña == 4:
            break
    
    if contraseña != '1234':
        for intento in range (1,3+1):
            print (F'CONTRASEÑA INCORRECTA, {intento} INTENTO(S) \n MAX. 3 INTENTOS.')
            contraseña = input ()
            largo_contraseña = len (contraseña)
            time.sleep (1)
            os.system ('cls')
            print ('CONECTANDO...')
            time.sleep (3)
            os.system ('cls')
            
            while largo_contraseña > 4 or largo_contraseña < 4  or largo_contraseña == '':
            
                print ('NO INGRESES MAS NI MENOS DE 4 NUMEROS O CARACTERES INCORRECTOS')
                print ('VUELVE A INTENTAR')
                contraseña = input ()
                largo_contraseña = len (contraseña)
                time.sleep (2)
                os.system ('cls')

                if contraseña == '1234' or largo_contraseña == 4:
                    time.sleep (1)
                    break
        
            if contraseña == '1234':
                time.sleep (1)
                break

        if intento == 3:
            print ('HAS ALCANZADO EL MAXIMO DE INTENTOS')
            print ('TU TARJETA HA SIDO BLOQUEADA')
            break

if contraseña == '1234':

    operacion = ''
    print ('CONEXION EXITOSA')
    time.sleep (1)
    os.system ('cls')
    while operacion != '4':
        print ('SELECCIONE OPERACIÓN')
        print ('')
        print ('1. CONSULTAR SALDO')
        print ('2. GIRO')
        print ('3. DEPOSITO')
        print ('4. SALIR')
        operacion = ''
        operacion =  input ()

        if operacion in ('1','2','3','4'):

            if operacion == '1':
                time.sleep (1)
                os.system('cls')
                print ('CARGANDO...')
                time.sleep (3)
                os.system ('cls')
                print (f'Su saldo es ${saldo}')
                time.sleep (3)
                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                msvcrt.getch()
                os.system('cls')

            elif operacion == '2':
                monto = ''
                time.sleep (1)
                os.system('cls')
                print ('CARGANDO...')
                time.sleep (3)
                os.system ('cls')
                while monto != '10':
                    print ('SELECCIONE UN MONTO')
                    print ('1. $5.000')
                    print ('2. $10.000')
                    print ('3. $15.000')
                    print ('4. $20.000')
                    print ('5. $25.000')
                    print ('6. $50.000')
                    print ('7. $100.000')
                    print ('8. $200.000')
                    print ('9. OTRO MONTO')
                    print ('10. VOLVER AL MENU')
                    monto = input ()

                    if monto in ('1','2','3','4','5','6','7','8','9','10'):

                        if monto == '1':
                            print ('PRESIONA BOTON VERDE PARA CONFIRMAR SU GIRO DE $5.000 (INTRO)')
                            msvcrt.getch()
                            os.system('cls')
                            
                            if saldo_cajero > 5000:
                            
                                if saldo > 5000:
                                    saldo = saldo - 5000

                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('TODO LISTO')
                                    time.sleep (3)
                                    os.system('cls')
                                    comprobante = ''

                                    while comprobante != '2':                                        
                                        print ('¿DESEA COMPROBANTE?')
                                        print ('1. SÍ')
                                        print ('2. NO')
                                        comprobante = input ()

                                        if comprobante in ('1','2'):

                                            if comprobante == '1':
                                                print ('ESPERE UN MOMENTO')
                                                time.sleep (3)
                                                os.system ('cls')
                                                print ('                        BANCOESTADO                                 ')
                                                print (time.strftime('FECHA: %d/%m/%y    HORA: %H:%M:%S    B7470    S001    SEC:4477'))
                                                print ('              COMPROBANTE DE GIRO DE EFECTIVO                     ')
                                                print ('                         CuentaRut                             ')
                                                print ('')
                                                print ('SUCURSAL 001 STGO. CENTRO.PRINCIPAL                              ')
                                                print ('')
                                                print ('NUMERO DE CUENTA :                                000245664821')
                                                print (time.strftime('FECHA CONTABLE   :                                    %d/%m/%y'))
                                                print ('')
                                                print ('MONTO GIRO       :                                       5.000')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('              CONSERVE ESTE COMPROBANTE                           ')
                                                print ('----------------------------------------------------------------')
                                                print ('             CONSULTAS   AL      600 200 80000') 
                                                print ('              Visitenos en www.bancoestado.cl')
                                                time.sleep (5)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                            elif comprobante == '2':
                                                print ('FINALIZANDO')
                                                time.sleep (3)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                        else:
                                            print ('INGRESE UN NUMERO CORRECTO')
                                            time.sleep (2)
                                            os.system ('cls')
                                else:
                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('NO TIENES EL SALDO SUFICIENTE')
                                    time.sleep (3)
                                    os.system ('cls')

                            
                            else:
                                print ('CAJERO NO POSEE SALDO SUFICIENTE PARA REALIZAR GIRO')

                        elif monto == '2':
                            print ('PRESIONA BOTON VERDE PARA CONFIRMAR SU GIRO DE $10.000 (INTRO)')
                            msvcrt.getch()
                            os.system('cls')
                            
                            if saldo_cajero >= 10000:
                            
                                if saldo >= 10000:    
                                    saldo = saldo - 10000

                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('TODO LISTO')
                                    time.sleep (3)
                                    os.system('cls')
                                    comprobante = ''

                                    while comprobante != '2':
                                        print ('¿DESEA COMPROBANTE?')
                                        print ('1. SÍ')
                                        print ('2. NO')
                                        comprobante = input ()

                                        if comprobante in ('1','2'):

                                            if comprobante == '1':
                                                print ('ESPERE UN MOMENTO')
                                                time.sleep (3)
                                                os.system ('cls')
                                                print ('                        BANCOESTADO                                 ')
                                                print (time.strftime('FECHA: %d/%m/%y    HORA: %H:%M:%S    B7470    S001    SEC:4477'))
                                                print ('              COMPROBANTE DE GIRO DE EFECTIVO                     ')
                                                print ('                         CuentaRut                             ')
                                                print ('')
                                                print ('SUCURSAL 001 STGO. CENTRO.PRINCIPAL                              ')
                                                print ('')
                                                print ('NUMERO DE CUENTA :                                000245664821')
                                                print (time.strftime('FECHA CONTABLE   :                                    %d/%m/%y'))
                                                print ('')
                                                print ('MONTO GIRO       :                                      10.000')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('              CONSERVE ESTE COMPROBANTE                           ')
                                                print ('----------------------------------------------------------------')
                                                print ('             CONSULTAS   AL      600 200 80000') 
                                                print ('              Visitenos en www.bancoestado.cl')
                                                time.sleep (5)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                            elif comprobante == '2':
                                                print ('FINALIZANDO')
                                                time.sleep (3)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                        else:
                                            print ('INGRESE UN NUMERO CORRECTO')                     
                                            time.sleep (2)
                                            os.system ('cls')
                                else:
                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('NO TIENES EL SALDO SUFICIENTE')
                                    time.sleep (3)
                                    os.system ('cls')


                            else:
                                print ('CAJERO NO POSEE SALDO SUFICIENTE PARA REALIZAR GIRO')                        
                        
                        elif monto == '3':
                            print ('PRESIONA BOTON VERDE PARA CONFIRMAR SU GIRO DE $15.000 (INTRO)')
                            msvcrt.getch()
                            os.system('cls')
                            
                            if saldo_cajero >= 15000:

                                if saldo >= 15000:
                                    saldo = saldo - 15000

                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('TODO LISTO')
                                    time.sleep (3)
                                    os.system('cls')
                                    comprobante = ''
                                    
                                    while comprobante != '2':
                                        
                                        print ('¿DESEA COMPROBANTE?')
                                        print ('1. SÍ')
                                        print ('2. NO')
                                        comprobante = input ()

                                        if comprobante in ('1','2'):

                                            if comprobante == '1':
                                                print ('ESPERE UN MOMENTO')
                                                time.sleep (3)
                                                os.system ('cls')
                                                print ('                        BANCOESTADO                                 ')
                                                print (time.strftime('FECHA: %d/%m/%y    HORA: %H:%M:%S    B7470    S001    SEC:4477'))
                                                print ('              COMPROBANTE DE GIRO DE EFECTIVO                     ')
                                                print ('                         CuentaRut                             ')
                                                print ('')
                                                print ('SUCURSAL 001 STGO. CENTRO.PRINCIPAL                              ')
                                                print ('')
                                                print ('NUMERO DE CUENTA :                                000245664821')
                                                print (time.strftime('FECHA CONTABLE   :                                    %d/%m/%y'))
                                                print ('')
                                                print ('MONTO GIRO       :                                      15.000')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('              CONSERVE ESTE COMPROBANTE                           ')
                                                print ('----------------------------------------------------------------')
                                                print ('             CONSULTAS   AL      600 200 80000') 
                                                print ('              Visitenos en www.bancoestado.cl')
                                                time.sleep (5)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                            elif comprobante == '2':
                                                print ('FINALIZANDO')
                                                time.sleep (3)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                        else:
                                            print ('INGRESE UN NUMERO CORRECTO')
                                            time.sleep (2)
                                            os.system ('cls')

                                else:
                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('NO TIENES EL SALDO SUFICIENTE')
                                    time.sleep (3)
                                    os.system ('cls')

                            else:
                                print ('CAJERO NO POSEE SALDO SUFICIENTE PARA REALIZAR GIRO')

                        elif monto == '4':
                            print ('PRESIONA BOTON VERDE PARA CONFIRMAR SU GIRO DE $20.000 (INTRO)')
                            msvcrt.getch()
                            os.system('cls')
                            
                            if saldo_cajero >= 20000:
                            
                                if saldo >= 20000:
                                    saldo = saldo - 20000
                                
                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('TODO LISTO')
                                    time.sleep (3)
                                    os.system('cls')
                                    comprobante = ''

                                    while comprobante != '2':
                                       
                                        print ('¿DESEA COMPROBANTE?')
                                        print ('1. SÍ')
                                        print ('2. NO')
                                        comprobante = input ()

                                        if comprobante in ('1','2'):

                                            if comprobante == '1':
                                                print ('ESPERE UN MOMENTO')
                                                time.sleep (3)
                                                os.system ('cls')
                                                print ('                        BANCOESTADO                                 ')
                                                print (time.strftime('FECHA: %d/%m/%y    HORA: %H:%M:%S    B7470    S001    SEC:4477'))
                                                print ('              COMPROBANTE DE GIRO DE EFECTIVO                     ')
                                                print ('                         CuentaRut                             ')
                                                print ('')
                                                print ('SUCURSAL 001 STGO. CENTRO.PRINCIPAL                              ')
                                                print ('')
                                                print ('NUMERO DE CUENTA :                                000245664821')
                                                print (time.strftime('FECHA CONTABLE   :                                    %d/%m/%y'))
                                                print ('')
                                                print ('MONTO GIRO       :                                      20.000')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('              CONSERVE ESTE COMPROBANTE                           ')
                                                print ('----------------------------------------------------------------')
                                                print ('             CONSULTAS   AL      600 200 80000') 
                                                print ('              Visitenos en www.bancoestado.cl')
                                                time.sleep (5)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                            elif comprobante == '2':
                                                print ('FINALIZANDO')
                                                time.sleep (3)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                        else:
                                            print ('INGRESE UN NUMERO CORRECTO')
                                            time.sleep (2)
                                            os.system ('cls')
                                else:
                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('NO TIENES EL SALDO SUFICIENTE')
                                    time.sleep (3)
                                    os.system ('cls')

                            else:
                                print ('CAJERO NO POSEE SALDO SUFICIENTE PARA REALIZAR GIRO')

                        elif monto == '5':
                            print ('PRESIONA BOTON VERDE PARA CONFIRMAR SU GIRO DE $25.000 (INTRO)')
                            msvcrt.getch()
                            os.system('cls')
                            
                            if saldo_cajero >= 25000:
                            
                                if saldo >= 25000:
                                    saldo = saldo - 25000
                                    
                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('TODO LISTO')
                                    time.sleep (3)
                                    os.system('cls')
                                    comprobante = ''
                                    
                                    while comprobante != '2':                                       
                                        print ('¿DESEA COMPROBANTE?')
                                        print ('1. SÍ')
                                        print ('2. NO')
                                        comprobante = input ()

                                        if comprobante in ('1','2'):

                                            if comprobante == '1':
                                                print ('ESPERE UN MOMENTO')
                                                time.sleep (3)
                                                os.system ('cls')
                                                print ('                        BANCOESTADO                                 ')
                                                print (time.strftime('FECHA: %d/%m/%y    HORA: %H:%M:%S    B7470    S001    SEC:4477'))
                                                print ('              COMPROBANTE DE GIRO DE EFECTIVO                     ')
                                                print ('                         CuentaRut                             ')
                                                print ('')
                                                print ('SUCURSAL 001 STGO. CENTRO.PRINCIPAL                              ')
                                                print ('')
                                                print ('NUMERO DE CUENTA :                                000245664821')
                                                print (time.strftime('FECHA CONTABLE   :                                    %d/%m/%y'))
                                                print ('')
                                                print ('MONTO GIRO       :                                      25.000')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('              CONSERVE ESTE COMPROBANTE                           ')
                                                print ('----------------------------------------------------------------')
                                                print ('             CONSULTAS   AL      600 200 80000') 
                                                print ('              Visitenos en www.bancoestado.cl')
                                                time.sleep (5)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                            elif comprobante == '2':
                                                print ('FINALIZANDO')
                                                time.sleep (3)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                        else:
                                            print ('INGRESE UN NUMERO CORRECTO')
                                            time.sleep (2)
                                            os.system ('cls')

                                else:
                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('NO TIENES EL SALDO SUFICIENTE')
                                    time.sleep (3)
                                    os.system ('cls')


                            else:
                                print ('CAJERO NO POSEE SALDO SUFICIENTE PARA REALIZAR GIRO')

                        elif monto == '6':
                            print ('PRESIONA BOTON VERDE PARA CONFIRMAR SU GIRO DE $50.000 (INTRO)')
                            msvcrt.getch()
                            os.system('cls')
                            
                            if saldo_cajero >= 50000:
                                
                                if saldo >= 50000:
                                    saldo = saldo - 50000
                                    
                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('TODO LISTO')
                                    time.sleep (3)
                                    os.system('cls')
                                    comprobante = ''

                                    while comprobante != '2':                                        
                                        print ('¿DESEA COMPROBANTE?')
                                        print ('1. SÍ')
                                        print ('2. NO')
                                        comprobante = input ()

                                        if comprobante in ('1','2'):

                                            if comprobante == '1':
                                                print ('ESPERE UN MOMENTO')
                                                time.sleep (3)
                                                os.system ('cls')
                                                print ('                        BANCOESTADO                                 ')
                                                print (time.strftime('FECHA: %d/%m/%y    HORA: %H:%M:%S    B7470    S001    SEC:4477'))
                                                print ('              COMPROBANTE DE GIRO DE EFECTIVO                     ')
                                                print ('                         CuentaRut                             ')
                                                print ('')
                                                print ('SUCURSAL 001 STGO. CENTRO.PRINCIPAL                              ')
                                                print ('')
                                                print ('NUMERO DE CUENTA :                                000245664821')
                                                print (time.strftime('FECHA CONTABLE   :                                    %d/%m/%y'))
                                                print ('')
                                                print ('MONTO GIRO       :                                      50.000')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('              CONSERVE ESTE COMPROBANTE                           ')
                                                print ('----------------------------------------------------------------')
                                                print ('             CONSULTAS   AL      600 200 80000') 
                                                print ('              Visitenos en www.bancoestado.cl')
                                                time.sleep (5)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                            elif comprobante == '2':
                                                print ('FINALIZANDO')
                                                time.sleep (3)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                        else:
                                            print ('INGRESE UN NUMERO CORRECTO')
                                            time.sleep (2)
                                            os.system ('cls')
                                else:
                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('NO TIENES EL SALDO SUFICIENTE')
                                    time.sleep (3)
                                    os.system ('cls')


                            else:
                                print ('CAJERO NO POSEE SALDO SUFICIENTE PARA REALIZAR GIRO')
                        
                        elif monto == '7':
                            print ('PRESIONA BOTON VERDE PARA CONFIRMAR SU GIRO DE $100.000 (INTRO)')
                            msvcrt.getch()
                            os.system('cls')
                            
                            if saldo_cajero >= 100000: 
                                
                                if saldo >= 100000:    
                                    saldo = saldo - 100000
                                    
                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('TODO LISTO')
                                    time.sleep (3)
                                    os.system('cls')
                                    comprobante = ''

                                    while comprobante != '2':                                      
                                        print ('¿DESEA COMPROBANTE?')
                                        print ('1. SÍ')
                                        print ('2. NO')
                                        comprobante = input ()

                                        if comprobante in ('1','2'):

                                            if comprobante == '1':
                                                print ('ESPERE UN MOMENTO')
                                                time.sleep (3)
                                                os.system ('cls')
                                                print ('                        BANCOESTADO                                 ')
                                                print (time.strftime('FECHA: %d/%m/%y    HORA: %H:%M:%S    B7470    S001    SEC:4477'))
                                                print ('              COMPROBANTE DE GIRO DE EFECTIVO                     ')
                                                print ('                         CuentaRut                             ')
                                                print ('')
                                                print ('SUCURSAL 001 STGO. CENTRO.PRINCIPAL                              ')
                                                print ('')
                                                print ('NUMERO DE CUENTA :                                000245664821')
                                                print (time.strftime('FECHA CONTABLE   :                                    %d/%m/%y'))
                                                print ('')
                                                print ('MONTO GIRO       :                                     100.000')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('              CONSERVE ESTE COMPROBANTE                           ')
                                                print ('----------------------------------------------------------------')
                                                print ('             CONSULTAS   AL      600 200 80000') 
                                                print ('              Visitenos en www.bancoestado.cl')
                                                time.sleep (5)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                            elif comprobante == '2':
                                                print ('FINALIZANDO')
                                                time.sleep (3)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                        else:
                                            print ('INGRESE UN NUMERO CORRECTO')
                                            time.sleep (2)
                                            os.system ('cls')
                                
                                else:
                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('NO TIENES EL SALDO SUFICIENTE')
                                    time.sleep (3)
                                    os.system ('cls')


                            else:
                                print ('CAJERO NO POSEE SALDO SUFICIENTE PARA REALIZAR GIRO')
                        
                        elif monto == '8':
                            print ('PRESIONA BOTON VERDE PARA CONFIRMAR SU GIRO DE $200.000 (INTRO)')
                            msvcrt.getch()
                            os.system('cls')
                            
                            if saldo_cajero >= 200000:    
                                
                                if saldo >= 200000:
                                    saldo = saldo - 200000

                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('TODO LISTO')
                                    time.sleep (3)
                                    os.system('cls')
                                    comprobante = ''
                                    
                                    while comprobante != '2':                                        
                                        print ('¿DESEA COMPROBANTE?')
                                        print ('1. SÍ')
                                        print ('2. NO')
                                        comprobante = input ()

                                        if comprobante in ('1','2'):

                                            if comprobante == '1':
                                                print ('ESPERE UN MOMENTO')
                                                time.sleep (3)
                                                os.system ('cls')
                                                print ('                        BANCOESTADO                                 ')
                                                print (time.strftime('FECHA: %d/%m/%y    HORA: %H:%M:%S    B7470    S001    SEC:4477'))
                                                print ('              COMPROBANTE DE GIRO DE EFECTIVO                     ')
                                                print ('                         CuentaRut                             ')
                                                print ('')
                                                print ('SUCURSAL 001 STGO. CENTRO.PRINCIPAL                              ')
                                                print ('')
                                                print ('NUMERO DE CUENTA :                                000245664821')
                                                print (time.strftime('FECHA CONTABLE   :                                    %d/%m/%y'))
                                                print ('')
                                                print ('MONTO GIRO       :                                     200.000')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('              CONSERVE ESTE COMPROBANTE                           ')
                                                print ('----------------------------------------------------------------')
                                                print ('             CONSULTAS   AL      600 200 80000') 
                                                print ('              Visitenos en www.bancoestado.cl')
                                                time.sleep (5)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                            elif comprobante == '2':
                                                print ('FINALIZANDO')
                                                time.sleep (3)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                        else:
                                            print ('INGRESE UN NUMERO CORRECTO')
                                            time.sleep (2)
                                            os.system ('cls')
                                                            
                                else:
                                    print ('PROCESANDO...')
                                    time.sleep (5)
                                    print ('NO TIENES EL SALDO SUFICIENTE')
                                    time.sleep (3)
                                    os.system ('cls')

                            else:
                                print ('CAJERO NO POSEE SALDO SUFICIENTE PARA REALIZAR GIRO')
                        
                        elif monto == '9':
                            os.system ('cls')
                            print ('ESCRIBA EL MONTO A DESEAR')
                            print ('máximo 200.000')
                            monto_eleccion = int (input ())
                            time.sleep(2)
                            print ('COMPROBANDO')
                            time.sleep (3)
                            os.system ('cls')
                            
                            while monto_eleccion > 200000 or monto_eleccion < 5000:
                                print ('INGRESE UN MONTO MENOR A $200.000 Y MAYOR A $5.000')
                                monto_eleccion = int (input())
                                time.sleep (2)
                                print ('COMPROBANDO...')
                                time.sleep (2)
                                os.system ('cls')
                            
                            if monto_eleccion <= 200000 and monto_eleccion >= 5000:                            
                                print (f'PRESIONA BOTON VERDE PARA CONFIRMAR SU GIRO DE ${monto_eleccion} (INTRO)')
                                msvcrt.getch()
                                os.system('cls')
                                
                                if saldo_cajero >= monto_eleccion:
                                    
                                    if saldo >= monto_eleccion:
                                        os.system('cls')
                                        print ('PROCESANDO...')
                                        time.sleep (5)
                                        os.system ('cls')
                                        saldo = saldo - monto_eleccion
                                        print ('TODO LISTO')
                                        time.sleep (2)
                                        os.system('cls')
                                        comprobante = ''
                                        
                                        while comprobante != '2':    
                                            print ('¿DESEA COMPROBANTE?')
                                            print ('1. SÍ')
                                            print ('2. NO')
                                            comprobante = input ()

                                            if comprobante in ('1','2'):

                                                if comprobante == '1':
                                                    print ('ESPERE UN MOMENTO')
                                                    time.sleep (3)
                                                    os.system ('cls')
                                                    print ('                        BANCOESTADO                                 ')
                                                    print (time.strftime('FECHA: %d/%m/%y    HORA: %H:%M:%S    B7470    S001    SEC:4477'))
                                                    print ('              COMPROBANTE DE GIRO DE EFECTIVO                     ')
                                                    print ('                         CuentaRut                             ')
                                                    print ('')
                                                    print ('SUCURSAL 001 STGO. CENTRO.PRINCIPAL                              ')
                                                    print ('')
                                                    print ('NUMERO DE CUENTA :                                000245664821')
                                                    print (time.strftime('FECHA CONTABLE   :                                    %d/%m/%y'))
                                                    print ('')
                                                    print (F'MONTO GIRO       :                                      {monto_eleccion}')
                                                    print ('')
                                                    print ('')
                                                    print ('')
                                                    print ('')
                                                    print ('              CONSERVE ESTE COMPROBANTE                           ')
                                                    print ('----------------------------------------------------------------')
                                                    print ('             CONSULTAS   AL      600 200 80000') 
                                                    print ('              Visitenos en www.bancoestado.cl')
                                                    time.sleep (5)
                                                    print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                    msvcrt.getch()
                                                    os.system ('cls')
                                                    break

                                                elif comprobante == '2':
                                                    print ('FINALIZANDO')
                                                    time.sleep (3)
                                                    print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                    msvcrt.getch()
                                                    os.system ('cls')
                                                    break

                                            else:
                                                print ('INGRESE UN NUMERO CORRECTO')
                                                time.sleep (2)
                                                os.system ('cls')
                                    else:
                                        print ('PROCESANDO...')
                                        time.sleep (5)
                                        os.system ('cls')
                                        print ('SALDO INSUFICIENTE')
                                        time.sleep (1)
                                        print ('NO SE PUEDE REALIZAR GIRO')
                                        time.sleep (1)
                                        os.system ('cls')

                                else:
                                    print ('CAJERO NO POSEE SALDO SUFICIENTE PARA REALIZAR GIRO')   
                        
                        elif monto == '10':
                            print ('VOLVIENDO...')                            
                            time.sleep (3)
                            os.system('cls')

                        else:
                            print ('INGRESE UN NUMERO CORRECTO')
                            time.sleep(3)
                            os.system ('cls')

            elif operacion == '3':
                eleccion = ''
                print ('CARGANDO...')
                time.sleep (3)
                os.system ('cls')
                while eleccion != '2':
                    print ('1. CONTINUAR DEPOSITO')
                    print ('2. CANCELAR')
                    eleccion = input ()
                    os.system ('cls')
                    
                    if eleccion in ('1','2'):

                        if eleccion == '1':
                            time.sleep (1)
                            print ('INGRESE DATOS DEL DESTINATARIO')
                            print ('')
                            print ('RUT (11111111-1)')
                            rut = input ()
                            largo_rut = len (rut)
                            time.sleep (3)
                            print ('VERIFICANDO...')
                            time.sleep (4)
                            os.system ('cls')

                            while largo_rut > 10 or largo_rut < 10 or largo_rut == '':
                                
                                if largo_rut > 10:
                                    print ('TE EXCEDISTE DE LA CANTIDAD DE CARACTERES PERMITIDO')
                                    print ('USA ESTE FORMATO (11111111-1)')
                                    rut = input ()
                                    largo_rut = len (rut)
                                    os.system ('cls')

                                elif largo_rut < 10:
                                    print ('NO INGRESASTE LA CANTIDAD DE CARACTERES REQUERIDA')
                                    print ('USA ESTE FORMATO (11111111-1)')
                                    rut = input ()
                                    largo_rut = len (rut)
                                    os.system ('cls')

                                elif largo_rut == '':
                                    print ('INGRESA RUT POR FAVOR')
                                    print ('USA ESTE FORMATO (11111111-1)')
                                    rut = input ()
                                    largo_rut = len (rut)
                                    os.system ('cls')

                                elif rut == '11111111-1':
                                    print ('NO ESCRIBAS EL EJEMPLO')

                                else:
                                    break

                            while rut == '11111111-1':
                                print ('NO ESCRIBAS EL EJEMPLO POR FAVOR')
                                print ('ESCRIBE UN RUT CORRECTO')
                                rut = input ('')
                                time.sleep (3)
                                os.system ('cls')
                                print ('VERIFICANDO...')
                                time.sleep (3)
                                os.system ('cls')

                            os.system ('cls')
                            print ('SELECCIONE UN MONTO A DEPOSITAR')
                            deposito = int (input ())
                            
                            while deposito > 200000 or deposito < 1000:
                                print ('INGRESA UN MONTO MENOR A $200.000 Y MAYOR A $1.000')
                                deposito = int (input())

                            if deposito <= 200000 and deposito >= 1000:                            
                                print (f'PRESIONA BOTON VERDE PARA CONFIRMAR SU DEPOSITO DE ${deposito} (INTRO)')
                                msvcrt.getch()
                                os.system('cls')
                                print ('INGRESE SOBRE')
                                time.sleep (5)
                                print ('COMPROBANDO...')
                                time.sleep (3)
                                os.system ('cls')
                                print ('LISTO')
                                print ('DEPOSITO EXITOSO')
                                time.sleep (3)
                                print ('')
                                
                                while comprobante != '2':
                                        print ('¿DESEA COMPROBANTE?')
                                        print ('1. SÍ')
                                        print ('2. NO')
                                        comprobante = input ()
                                        os.system ('cls')

                                        if comprobante in ('1','2'):

                                            if comprobante == '1':
                                                print ('ESPERE UN MOMENTO')
                                                time.sleep (3)
                                                os.system ('cls')
                                                print ('                        BANCOESTADO                                 ')
                                                print (time.strftime('FECHA: %d/%m/%y    HORA: %H:%M:%S    B7470    S001    SEC:4477'))
                                                print ('              COMPROBANTE DE DEPOSITO DE EFECTIVO                     ')
                                                print ('                         CuentaRut                             ')
                                                print ('')
                                                print ('SUCURSAL 001 STGO. CENTRO.PRINCIPAL                              ')
                                                print ('')
                                                print ('NUMERO DE CUENTA :                                000245664821')
                                                print ('N. CUENTA DESTINATARIO :                          000125465117')
                                                print (f'RUT DESTINATARIO  :                                 {rut}')
                                                print (time.strftime('FECHA CONTABLE   :                                    %d/%m/%y'))
                                                print ('')
                                                print (F'MONTO DEPOSITO :                                         {deposito}')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('')
                                                print ('              CONSERVE ESTE COMPROBANTE                           ')
                                                print ('----------------------------------------------------------------')
                                                print ('             CONSULTAS   AL      600 200 80000') 
                                                print ('              Visitenos en www.bancoestado.cl')
                                                time.sleep (5)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                            elif comprobante == '2':
                                                print ('FINALIZANDO')
                                                time.sleep (3)
                                                print ('PRESIONE CUALQUIER BOTON PARA VOLVER')
                                                msvcrt.getch()
                                                os.system ('cls')
                                                break

                                        else:
                                            print ('INGRESE UN NUMERO CORRECTO')                     
                                            time.sleep (2)
                                            os.system ('cls')

                        elif eleccion == '2':
                            print ('VOLVIENDO...')
                            time.sleep (3)
                            os.system ('cls')


                    else:
                        print ('INGRESE UN NUMERO CORRECTO')
                        time.sleep (3)
                        os.system ('cls')  
                    
            elif operacion == '4':
                    time.sleep (1)
                    os.system ('cls')
                    print ('RETIRE SU TARJETA POR FAVOR')
                    time.sleep (5)
                    os.system ('cls')
                    print ('HASTA PRONTO')
                    time.sleep (3)
                    os.system ('cls')                
