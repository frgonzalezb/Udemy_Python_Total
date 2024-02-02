from random import choice


def lanzar_moneda():
    return choice(['Cara', 'Cruz'])


def probar_suerte(resultado, lista):
    if resultado == 'Cara':
        print('La lista se autodestruirá')
        return lista.clear()
    else:
        print('La lista fue salvada')


lista_numeros = [1, 2, 3, 4, 5]
probar_suerte(lanzar_moneda(), lista_numeros)
