'''
Decoradores y generadores para el programa.
'''


AREAS = {
    'P': 'Perfumería',
    'F': 'Farmacia',
    'C': 'Cosmética',
}


def decorar_numero(funcion):
    '''
    Añade un texto adicional antes y después del número de atención 
    obtenido desde otra función.
    '''
    def funcion_a_decorar(parametro):
        print('Su turno es el ')
        funcion(parametro)
        print('Por favor, aguarde y será atendido')
    
    return funcion_a_decorar

