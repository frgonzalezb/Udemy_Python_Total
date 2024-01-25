'''
PROYECTO DEL DÍA
"CUENTA BANCARIA"

Ver pdf y/o video para mayor información.
'''

from os import system as sys
from random import randint
from colorama import Fore


# Colores
RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
RESET = Fore.RESET


class Persona:
    def __init__(self, nombre: str, apellido: str):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, cuenta: str, balance: dict):
        self.cuenta = cuenta
        self.balance = balance

    def __str__(self):
        cliente = self.nombre + ' ' +  self.apellido
        cuenta = self.cuenta
        balance = self.balance
        return f'Balance de la cuenta {cuenta} de {cliente}:\n\n{balance}'
    
    def depositar(self):
        monto = input('Ingrese un monto a depositar: $')
        respuesta = f'Ha depositado ${monto} en su cuenta.'
        return GREEN + respuesta + RESET
    
    def retirar(self):
        monto = input('Ingrese el monto a retirar: $')
        respuesta = f'Ha retirado ${monto} de su cuenta.'
        return GREEN + respuesta + RESET


def limpiar_consola():
    sys('cls')


def esperar_usuario():
    mensaje = 'Presione ENTER para continuar...'
    input(MAGENTA + mensaje + RESET)


def confirmar_accion(pregunta):
    opcion = input(f'{pregunta} (s/n): ')
    return True if opcion.lower() == 's' else False


def mostrar_alerta(mensaje):
    print(YELLOW + 'ATENCIÓN: ' + mensaje + RESET)


def mostrar_error(mensaje):
    print(RED + 'ERROR: ' + mensaje + RESET)


def formatear_titulo(texto, caracter_borde='#'):
    borde = f'{BLUE}{caracter_borde * len(texto)}{RESET}'
    return f'{borde}\n{texto}\n{borde}'


def mostrar_titulo(texto):
    titulo = formatear_titulo(texto.upper())
    print(titulo + '\n')


def mostrar_introduccion():
    saludo = 'Nos alegra que desee abrir una cuenta en nuestro banco.'
    info = 'Para continuar, necesitamos saber algunos datos sobre Ud.'
    print(YELLOW + saludo + '\n' + info + RESET + '\n')


def generar_nro_cuenta():
    return str(randint(100000000, 999999999))


def abrir_cuenta():
    mostrar_introduccion()
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    nro_cuenta = generar_nro_cuenta()
    print(f'¡Felicidades, {nombre} {apellido}!')
    print(f'Su cuenta N° {nro_cuenta} ha sido creada exitosamente.')


def ejecutar_programa():
    while True:
        limpiar_consola()
        mostrar_titulo('¡Bienvenido a Banco Faladeuda!')
        abrir_cuenta()
        break


ejecutar_programa()
