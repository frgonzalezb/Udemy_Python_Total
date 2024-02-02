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


def generar_numero(letra_area):
    num = 0
    while True:
        yield f'{letra_area}-{num:02d}'
        num = (num + 1) % 100


gen_perfumeria = generar_numero('P')
gen_farmacia = generar_numero('F')
gen_cosmetica = generar_numero('C')


@decorar_numero
def obtener_numero(letra_area):
    if letra_area == 'P':
        print(next(gen_perfumeria))
    elif letra_area == 'F':
        print(next(gen_farmacia))
    elif letra_area == 'C':
        print(next(gen_cosmetica))
    else:
        utilidades.mostrar_error('Valor desconocido.')
