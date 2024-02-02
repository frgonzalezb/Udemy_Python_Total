'''
JUEGO 'ADIVINA EL NÚMERO'

CONSIGNA:
- El usuario debe ingresar su nombre.
- El usuario debe ingresar un número 'N' entre el 1 y el 100.
- El programa seleccionará un número secreto '?' entre 1 y 100.
- El usuario tiene 8 intentos para ganar.
- Si se agotan los intentos = Game Over!
- El programa debe incluir validadores:
    - N no puede ser menor a 1 ni mayor a 100.
    - Si N < ?, el programa debe indicar 'intento fallido' y
      dar la pista de que 'N es menor a ?'
    - Si N > ?, el programa debe indicar 'intento fallido' y
      dar la pista de que 'N es mayor a ?'
    - Si N = ?, el programa debe terminar, mostrando una frase 
      de victoria y mostrar la cantidad de intentos.
'''

from random import randint
from colored import Fore, Style


# Colores
RED = Fore.red
YELLOW = Fore.yellow
GREEN = Fore.green
BLUE = Fore.blue
RESET = Style.reset


def mostrar_mensaje_intentos(contador):
    if contador > 1:
        print(f'\nTienes {YELLOW}{contador} intentos{RESET} para adivinar el número secreto.')
    else:
        print(f'\n¡Te queda {RED}sólo 1 intento{RESET} para adivinar el número secreto!')


def mostrar_mensaje_victoria(jugador, contador):
    total = 8 - contador
    print(f'\n{BLUE}¡Felicitaciones, {jugador}!{RESET}')
    print(f'¡Has descubierto el número secreto {GREEN}{num_secreto}{RESET} en {YELLOW}{total}{RESET} intentos!')


def mostrar_mensaje_derrota(jugador, num_secreto):
    print(f'Lo siento, {jugador}. Ya no tienes más intentos.')
    print(f'El número secreto era: {num_secreto}')
    print('¡GAME OVER!')


def ejecutar_juego(contador, num_secreto, jugador):
    while contador > 0:
        mostrar_mensaje_intentos(contador)
        
        intento = input('Ingresa un número entero entre 1 y 100: ')
        
        if not intento.isnumeric():
            contador -= 1
            print(f'{RED}ERROR:{RESET} "{intento}" no es una entrada válida.')
            continue

        intento = int(intento)

        if intento < 1 or intento > 100:
            contador -= 1
            print(f'\n{RED}¡Has fallado!{RESET} El número {YELLOW}{intento}{RESET} está fuera del rango.')
        elif intento < num_secreto:
            contador -= 1
            print(f'\n{RED}¡Has fallado!{RESET} El número {YELLOW}{intento}{RESET} es {GREEN}menor{RESET} al número secreto.')
        elif intento > num_secreto:
            contador -= 1
            print(f'\n{RED}¡Has fallado!{RESET} El número {YELLOW}{intento}{RESET} es {GREEN}mayor{RESET} al número secreto.')
        elif intento == num_secreto:
            mostrar_mensaje_victoria(jugador, contador)
            break
    else:
        mostrar_mensaje_derrota(jugador, num_secreto)


contador = 8
num_secreto = randint(1, 100)
jugador = input(f'{BLUE}¡Bienvenido, jugador!{RESET}\nIngresa tu nombre: ')

ejecutar_juego(contador, num_secreto, jugador)
