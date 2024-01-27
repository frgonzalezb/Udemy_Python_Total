# Script para entender los decoradores
'''
def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


def una_funcion(funcion):
    return funcion


una_funcion(mayuscula('probando'))
'''


'''
def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())


    def minuscula(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minuscula
    

operacion = cambiar_letras('may')
operacion('palabra')
'''


def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion


@decorar_saludo
def mayuscula(texto):
    print(texto.upper())


@decorar_saludo
def minuscula(texto):
    print(texto.lower())


mayuscula('python')

# Básicamente, un decorador es una función que envuelve a otras funciones.
# Permite añadir más funcionalidades a funciones similares, evitando la
# redundancia de código entre ellas.

# Para mejor comprensión, lo siguiente devuelve exactamente lo mismo:

def mayusculas(texto):
    print(texto.upper())

mayuscula_decorada = decorar_saludo(mayusculas)
mayuscula_decorada('python')
