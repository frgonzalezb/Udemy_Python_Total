def suma():
    a = int(input('Ingrese un número: '))
    b = int(input('Ingrese otro número: '))
    print(a + b)
    print('Gracias por sumar')


'''
try:
    # Código que queremos probar
    suma()
except:
    # Código a ejecutar si hay un error
    print('Algo no ha salido bien')
else:
    # Código a ejecutar si no hay un error
    print('Hiciste todo bien')
finally:
    # Código que se va a ejecutar de todos modos
    print('Eso fue todo')
'''

try:
    suma()
except TypeError as e:
    print(f'No puedes sumar texto y números. Detalle: {e}')
except ValueError as e:
    print(f'Lo que has ingresado no es un número. Detalle: {e}')


def pedir_numero():
    while True:
        try:
            numero = int(input('Dame un número: '))
        except:
            print('Ese no es un número')
        else:
            print(f'Ingresate el número {numero}')
            break


pedir_numero()
