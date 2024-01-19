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
from colorama import Fore # Porque... ¿por qué no? 😁


def mostrar_mensaje_intentos(contador):
    if contador > 1:
        print(f'\nTienes {Fore.YELLOW}{contador} intentos{Fore.RESET} para adivinar el número secreto.')
    else:
        print(f'\n¡Te queda {Fore.RED}sólo 1 intento{Fore.RESET} para adivinar el número secreto!')


def mostrar_mensaje_victoria(jugador, contador):
    total = 8 - contador
    print(f'\n{Fore.BLUE}¡Felicitaciones, {jugador}!{Fore.RESET}')
    print(f'¡Has descubierto el número secreto {Fore.GREEN}{num_secreto}{Fore.RESET} en {Fore.YELLOW}{total}{Fore.RESET} intentos!')


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
            print(f'{Fore.RED}ERROR:{Fore.RESET} "{intento}" no es una entrada válida.')
            continue

        intento = int(intento)

        if intento < 1 or intento > 100:
            contador -= 1
            print(f'\n{Fore.RED}¡Has fallado!{Fore.RESET} El número {Fore.YELLOW}{intento}{Fore.RESET} está fuera del rango.')
        elif intento < num_secreto:
            contador -= 1
            print(f'\n{Fore.RED}¡Has fallado!{Fore.RESET} El número {Fore.YELLOW}{intento}{Fore.RESET} es {Fore.GREEN}menor{Fore.RESET} al número secreto.')
        elif intento > num_secreto:
            contador -= 1
            print(f'\n{Fore.RED}¡Has fallado!{Fore.RESET} El número {Fore.YELLOW}{intento}{Fore.RESET} es {Fore.GREEN}mayor{Fore.RESET} al número secreto.')
        elif intento == num_secreto:
            mostrar_mensaje_victoria(jugador, contador)
            break
    else:
        mostrar_mensaje_derrota(jugador, num_secreto)


contador = 8
num_secreto = randint(1, 100)
jugador = input(f'{Fore.BLUE}¡Bienvenido, jugador!{Fore.RESET}\nIngresa tu nombre: ')

ejecutar_juego(contador, num_secreto, jugador)
