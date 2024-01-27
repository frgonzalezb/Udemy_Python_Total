'''
Decoradores y generadores para el programa.
'''


import utilidades


def decorar_numero(funcion):
    '''
    Añade un texto adicional antes y después del número de atención 
    obtenido desde otra función.
    '''
    def funcion_a_decorar(parametro):
        print(f'{utilidades.YELLOW}Su turno es el ')
        funcion(parametro)
        print(f'Por favor, aguarde y será atendido{utilidades.RESET}')
    
    return funcion_a_decorar


def generar_numero():
    n = 0
    while True:
        n += 1
        yield n
            


@decorar_numero
def obtener_numero(letra_area):
    generador = generar_numero()
    numero = next(generador)
    if numero < 10:
        print(letra_area + '-' + '0' + str(numero))
    else:
        print(letra_area + '-' + str(numero))
