def hr(character='-', length=80, pre_margin=False, post_margin=False):
    '''
    Simple low-cost <hr> tag for console.
    '''
    rule = character * length
    margin = '\n'

    if pre_margin:
        print(margin + rule)
    elif post_margin:
        print(rule + margin)
    elif pre_margin and post_margin:
        print(margin + rule + margin)
    else:
        print(rule)


def while_monedas(valor):
    monedas = valor

    while monedas > 0:
        print(f'Tengo {monedas} monedas.')
        monedas -= 1
    else:
        print('No tengo más monedas.')


def while_respuesta(valor):
    respuesta = valor

    while respuesta == 's':
        respuesta = input('¿Quieres seguir? (s/n): ')
    else:
        print('Adiós.')


while_monedas(5)
hr()
while_respuesta('s')