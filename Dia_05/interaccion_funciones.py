from random import shuffle


def mezclar_palitos(lista):
    shuffle(lista)
    return lista


def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un número del 1 al 4: ')

    return int(intento)


def comprobar_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('¡A lavar los platos!')
    else:
        print('Te has salvado por esta vez.')

    print(f'Te ha tocado {lista[intento - 1]}')


# Ejemplo de uso
palitos = ['-', '--', '---', '----']
palitos_mezclados = mezclar_palitos(palitos)
seleccion = probar_suerte()
comprobar_intento(palitos_mezclados, seleccion)
