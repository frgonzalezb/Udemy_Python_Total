'''
Popurrí de constantes y funciones utilitarias de uso general.
'''


from colored import Fore, Style
from os import system as sys


# Colores
RED = Fore.red
YELLOW = Fore.yellow
GREEN = Fore.green
BLUE = Fore.blue
MAGENTA = Fore.magenta
RESET = Style.reset


def limpiar_consola():
    sys('cls')


def esperar_usuario():
    mensaje = 'Presione ENTER para continuar...'
    input(MAGENTA + mensaje + RESET)


def formatear_titulo(texto, caracter_borde='#'):
    borde = f'{BLUE}{caracter_borde * len(texto)}{RESET}'
    return f'{borde}\n{texto}\n{borde}'


def mostrar_titulo(texto):
    titulo = formatear_titulo(texto.upper())
    print(titulo + '\n')


def mostrar_mensaje(mensaje):
    print(GREEN + mensaje + RESET)


def mostrar_alerta(mensaje):
    print(YELLOW + 'ATENCIÓN: ' + mensaje + RESET)


def mostrar_error(mensaje):
    print(RED + 'ERROR: ' + mensaje + RESET)


def escoger_opcion():
    opcion = input(f'{MAGENTA}Ingrese el número de su opción:{RESET} ')

    if not opcion.isnumeric():
        mostrar_error(f'La opción "{opcion}" no es válida.')
        return
    
    return int(opcion)


def mostrar_opciones(opciones: list):
    for numero, opcion in enumerate(opciones):
        texto = f'[{numero + 1}] - {opcion}'
        if numero in max(enumerate(opciones)):
            print(texto + '\n')
        else:
            print(texto)


def confirmar_accion(pregunta):
    opcion = input(f'{YELLOW}{pregunta} (s/n):{RESET} ')
    return True if opcion.lower() == 's' else False
