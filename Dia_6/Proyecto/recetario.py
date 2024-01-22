'''
PROYECTO DEL DÍA: RECETARIO


PRE-CONSIGNA:
Crear los directorios y archivos necesarios, según video o pdf


CONSIGNA (lo que debe hacer el código):

1. Dar la bienvenida al usuario

2. Informar:
    - la ruta de acceso al directorio donde se encuentra
      la carpeta de recetas ("Las recetas están en... ").
    - la cantidad total de recetas que hay en el directorio
      ("Tienes [x] recetas")

3. Indicar las opciones que el usuario puede hacer:
    [1] - leer receta
    [2] - crear receta
    [3] - crear categoría
    [4] - eliminar receta
    [5] - eliminar categoría
    [6] - finalizar programa

4. La opción [1] debe:
    - pedir al usuario la categoría a escoger
      (carnes, ensaladas, postres, etc.)
    - mostrar recetas
    - pedir al usuario la receta a escoger
    - leer receta

5. La opción [2] debe:
    - pedir al usuario la categoría a escoger
      (carnes, ensaladas, postres, etc.)
    - pedir al usuario el nombre para la receta
    - crear el archivo
    - pedir al usuario el contenido para la receta
    - escribir el archivo

6. La opción [3] debe:
    - pedir al usuario el nombre para la categoria
    - crear el directorio para la categoria

7. La opción [4] debe:
    - lo mismo que en [1], excepto el último paso
    - eliminar receta (el archivo)

8. La opción [5] debe:
    - pedir al usuario la categoría a escoger
    - eliminar la categoría (el directorio)

TIPS:
- Envolver el código en un loop while (para que el usuario pueda
  salir con la opción [6]). El loop debe repetirse desde el menú.
- Limpiar la consola de tanto en tanto.
- Buscar en la documentación más métodos de Python. No hay pecado
  en usar cosas más avanzadas aún no vistas. 😎
- Compartimentar el código en tantas funciones como sean necesarias.
'''

import os

from os import system as sys
from pathlib import Path
from colorama import Fore


def limpiar_consola():
    sys('cls')


def dar_bienvenida():
    return


def informar_ruta():
    return


def mostrar_total_recetas():
    return


def mostrar_menu():
    return


def leer_receta():
    return


def crear_receta():
    return


def crear_categoria():
    return


def eliminar_receta():
    return


def eliminar_categoria():
    return


def finalizar_programa():
    return True


def mostrar_adios():
    return


def ejecutar_programa():
    salir = False
    while not salir:
        # Aquí va el código del 'ejecutable'
        pass


ejecutar_programa()
