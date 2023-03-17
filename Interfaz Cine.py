print('Bienvenido a Cinemark')
print('----------------------------')
print('Ingrese su usuario')
usuario=input()
print('----------------------------')
print('Ingrese su contraseña')
clave=input()
print('----------------------------')
print(f'Bienvenido {usuario}, hoy jueves te ofrecemos un 20% de descuento en cualquier pelicula en cartelera 2D')
print('Escribe el nombre de la pelicula')
pelicula=input()
print('----------------------------')
print('Cuantas entradas deseas?')
entradas=float(input())
print('----------------------------')
v_entrada_n=4000
v_entrada_d=4000-(v_entrada_n*0.2)
v_t_entrada=v_entrada_d*entradas
sin_d=4000*entradas
print('Los horarios disponibles para tu funcion son a las 12:40pm - 15:20pm - 17:30pm - 19:15pm, Porfavor seleccione uno')
horario=input()
print('------------------------------------------')
print('Los datos de tu compra son:')
print(f'Pelicula: {pelicula} Version 2D')
print(f'Hora de su funcion {horario}')
print(f'Entradas: {entradas}')
print(f'Valor total sin descuento: {sin_d}')
print(f'Valor a pagar con descuento: {v_t_entrada}')
print('------------------------------------------')
print('Confirmando compra....')
print('-------------------------------------')
print(f'Compra exitosa, gracias por preferirnos {usuario}')



















