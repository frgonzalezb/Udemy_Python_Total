'''
'cls' para Window
'clear' para Mac/Linux
'''

from os import system as sys


nombre = input('Tu nombre: ')
edad = input('Tu edad: ')

sys('cls')

print(f'Tu nombre es {nombre} y tu edad es {edad}')
