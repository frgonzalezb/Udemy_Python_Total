'''
Caso:
Los vendedores reciben un 13% de comisión por ventas.
El programa debe pedir al usuario su nombre y el monto total de ventas.
Programa debe responder con una frase del tipo: "Juan, este mes ganaste $650".
'''

vendedor = input('Ingrese su nombre: ')
monto = float(input('Ingrese el monto total de sus ventas: CLP '))
comision = round(monto * 0.13)

respuesta = f'Estimado {vendedor}, su comisión por ventas es de CLP {comision}'
print(respuesta)
