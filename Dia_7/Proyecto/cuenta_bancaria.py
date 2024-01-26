'''
PROYECTO DEL DÍA
"CUENTA BANCARIA"

Ver pdf y/o video para mayor información.
'''

from os import system as sys
from random import randint
from colored import Fore, Style


# Colores
RED = Fore.red
YELLOW = Fore.yellow
GREEN = Fore.green
BLUE = Fore.blue
MAGENTA = Fore.magenta
RESET = Style.reset


class Persona:
    def __init__(self, nombre: str, apellido: str):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre: str, apellido: str, cuenta: str, balance: int):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta
        self.balance = balance

    def __str__(self):
        cliente = f'El cliente {self.nombre + ' ' +  self.apellido} '
        cuenta = f'con la cuenta N° {self.cuenta} '
        balance = f'tiene un saldo de ${self.balance}.-'
        return YELLOW + cliente + cuenta + balance + RESET + '\n'
    
    def depositar(self, monto):
        self.balance += monto
    
    def retirar(self, monto):
        if monto > self.balance:
            return False
        self.balance -= monto
        return True


def limpiar_consola():
    sys('cls')


def esperar_usuario():
    mensaje = 'Presione ENTER para continuar...'
    input(MAGENTA + mensaje + RESET)


def confirmar_accion(pregunta):
    opcion = input(f'{YELLOW}{pregunta} (s/n):{RESET} ')
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
    saludo = 'Nos alegra que desee abrir una cuenta en Banco Faladeuda.'
    info = 'Para continuar, necesitamos saber algunos datos sobre Ud.'
    print(YELLOW + saludo + '\n' + info + RESET + '\n')


def generar_nro_cuenta():
    return str(randint(100000000, 999999999))


def crear_cliente():
    mostrar_introduccion()
    nombre = input('Ingrese su nombre: ').title()
    apellido = input('Ingrese su apellido: ').title()
    nro_cuenta = generar_nro_cuenta()
    cliente = Cliente(
        nombre=nombre,
        apellido=apellido,
        cuenta=nro_cuenta,
        balance=0
    )
    mensaje_1 = f'¡Felicidades, {nombre} {apellido}!'
    mensaje_2 = f'Su cuenta N° {nro_cuenta} ha sido creada exitosamente.'
    print(GREEN + '\n' + mensaje_1 + '\n' + mensaje_2 + '\n' + RESET)
    esperar_usuario()

    return cliente


def escoger_opcion():
    opcion = input(f'{MAGENTA}Ingrese el número de su opción:{RESET} ')

    if not opcion.isnumeric():
        mostrar_error(f'La opción "{opcion}" no es válida.')
        return
    
    return int(opcion)


def mostrar_opciones(opciones: list):
    for numero, opcion in enumerate(opciones):
        texto = f'[{numero}] - {opcion}'
        if numero in max(enumerate(opciones)):
            print(texto + '\n')
        else:
            print(texto)


def imprimir_cliente(cliente):
    limpiar_consola()
    mostrar_titulo('Ver datos del cliente')
    print(cliente)
    esperar_usuario()


def depositar_fondos(cliente):
    while True:
        limpiar_consola()
        mostrar_titulo('Depositar fondos a la cuenta')

        monto = input(f'{MAGENTA}Ingrese el monto a depositar:{RESET} $')

        if not monto.isnumeric():
            mostrar_error(f'El valor ingresado "{monto}" no es válido.')
            esperar_usuario()
            continue

        cliente.depositar(int(monto))

        print(f'{GREEN}La operación ha sido realizada exitosamente.{RESET}')
        esperar_usuario()
        break
    

def retirar_fondos(cliente):
    while True:
        limpiar_consola()
        mostrar_titulo('Retirar fondos de la cuenta')

        monto = input(f'{MAGENTA}Ingrese el monto a retirar:{RESET} $')

        if not monto.isnumeric():
            mostrar_error(f'El valor ingresado "{monto}" no es válido.')
            esperar_usuario()
            continue

        operacion_exitosa = cliente.retirar(int(monto))

        if not operacion_exitosa:
            mensaje_1 = f'El monto ingresado excede a su saldo. '
            mensaje_2 = f'Su saldo actual es de ${cliente.balance}.-'
            mostrar_error(mensaje_1 + mensaje_2)
            esperar_usuario()
            continue

        print(f'{GREEN}La operación ha sido realizada exitosamente.{RESET}')
        esperar_usuario()
        break


def mostrar_menu_principal(cliente):
    salir = False
    while not salir:
        limpiar_consola()
        mostrar_titulo('Menú Principal')
        mostrar_opciones([
            'Salir',
            'Ver datos del cliente',
            'Depositar fondos a la cuenta',
            'Retirar fondos de la cuenta',
        ])
        opcion = escoger_opcion()

        if opcion == 0:
            salir = confirmar_accion('¿Desea salir?')
        elif opcion == 1:
            imprimir_cliente(cliente)
        elif opcion == 2:
            depositar_fondos(cliente)
        elif opcion == 3:
            retirar_fondos(cliente)
        else:
            continue


def ejecutar_programa():
    limpiar_consola()
    mostrar_titulo('¡Bienvenido a Banco Faladeuda!')
    
    cliente = crear_cliente()
    
    mostrar_menu_principal(cliente)


ejecutar_programa()
