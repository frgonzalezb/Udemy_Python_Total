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


# Colores
RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
CYAN = Fore.CYAN
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
RESET = Fore.RESET

# Directorio base
DIRECTORIO_BASE = Path(Path.home(), 'Recetas')


############################## UTILIDADES ##############################

def limpiar_consola():
    sys('cls')


def continuar():
    input('Presione ENTER para continuar...')


def confirmar_accion(pregunta):
    opcion = input(f'{pregunta} (s/n): ')
    return True if opcion.lower() == 's' else False


def mostrar_alerta(mensaje, irreversibilidad=False):
    if irreversibilidad:
        irreversible = 'Esta acción es irreversible. '
        print(YELLOW + 'ATENCIÓN: ' + irreversible + mensaje + RESET)
    else:
        print(YELLOW + 'ATENCIÓN: ' + mensaje + RESET)


def mostrar_error(mensaje):
    print(RED + 'ERROR: ' + mensaje + RESET)
    continuar()


def formatear_titulo(texto, caracter_borde='#'):
    borde = f'{GREEN}{caracter_borde * len(texto)}{RESET}'
    return f'{borde}\n{texto}\n{borde}'


def mostrar_titulo(texto):
    titulo = formatear_titulo(texto.upper())
    print(titulo + '\n')
    

def entregar_informaciones(directorio_base):
    if not directorio_base:
        # Salir si no se encuentra "Recetas"
        # Se podría implementar un "instalador" a futuro
        mostrar_error('No se encuentra "Recetas" en su directorio base.')
        exit()

    cantidad = 0
    for txt in directorio_base.glob('**/*.txt'):
        cantidad += 1

    ubicacion = f'Las recetas están en {directorio_base}'
    mensaje = f'Este recetario contiene un total de {cantidad} recetas.'
    print(ubicacion + '\n' + mensaje + '\n')


def mostrar_introduccion(directorio_base):
    limpiar_consola()
    mostrar_titulo('¡Bienvenido al Recetario del Chef!')
    entregar_informaciones(directorio_base)
    continuar()


def mostrar_menu_principal():
    '''
    Imprime en consola el menú principal de la aplicación.
    '''
    limpiar_consola()
    mostrar_titulo('Menú Principal')
    opciones = [
        'Leer receta',
        'Crear receta',
        'Crear categoría',
        'Eliminar receta',
        'Eliminar categoría',
        'Salir del recetario',
    ]
    for numero, opcion in enumerate(opciones):
        texto = f'[{numero+1}] - {opcion}'
        if numero in max(enumerate(opciones)):
            print(texto + '\n')
        else:
            print(texto)


def escoger_opcion():
    opcion = input('Ingrese el número de su opción: ')

    if not opcion.isnumeric():
        mostrar_error(f'La opción "{opcion}" no es válida.')
        return
    
    return int(opcion)


def obtener_categorias(directorio_base):
    categorias = os.listdir(directorio_base)
    categorias.insert(0, 'Volver al menú anterior')

    for numero, categoria in enumerate(categorias):
        texto = f'[{numero}] - {categoria}'
        if numero in max(enumerate(categorias)):
            print(texto + '\n')
        else:
            print(texto)

    return list(enumerate(categorias))


def obtener_recetas(directorio_base, categoria):
    ruta = Path(directorio_base, categoria)
    recetas = os.listdir(ruta)
    recetas.insert(0, 'Volver al menú anterior')

    for numero, categoria in enumerate(recetas):
        texto = f'[{numero}] - {categoria}'
        if numero in max(enumerate(recetas)):
            print(texto + '\n')
        else:
            print(texto)

    return list(enumerate(recetas))


######################### SUBMENÚS SECUNDARIOS #########################

def abrir_receta(directorio_base, categoria, receta):
    while True:
        limpiar_consola()
        mostrar_titulo(receta)
        ruta = Path(directorio_base, categoria, receta)
        archivo = open(str(ruta))
        print(archivo.read())
        volver = confirmar_accion('¿Desea volver atrás?')
        if volver:
            archivo.close()
            break
    return


def abrir_categoria(directorio_base, categoria):
    while True:
        limpiar_consola()
        mostrar_titulo(categoria)
        recetas = obtener_recetas(directorio_base, categoria)
        opcion = escoger_opcion()
        
        if opcion is None:
            continue
        elif opcion == 0:
            break
        elif opcion > 0:
            for numero, receta in recetas:
                if numero == opcion:
                    abrir_receta(directorio_base, categoria, receta)
    return


########################## SUBMENÚS PRIMARIOS ##########################

def ir_a_leer_receta(directorio_base):
    while True:
        limpiar_consola()
        mostrar_titulo('Leer receta')
        categorias = obtener_categorias(directorio_base)
        opcion = escoger_opcion()

        if opcion is None:
            continue
        elif opcion == 0:
            break
        elif opcion > 0:
            for numero, categoria in categorias:
                if numero == opcion:
                    abrir_categoria(directorio_base, categoria)
    return


def ir_a_crear_receta(directorio_base):
    while True:
        limpiar_consola()
        mostrar_titulo('Crear receta')
        categorias = obtener_categorias(directorio_base)
        opcion = escoger_opcion()

        if opcion is None:
            continue
        elif opcion == 0:
            break
        elif opcion > 0:
            for numero, categoria in categorias:
                if numero == opcion:
                    abrir_categoria(directorio_base, categoria)


def ir_a_crear_categoria():
    return


def ir_a_eliminar_receta():
    limpiar_consola()
    mostrar_alerta('Se eliminará esta receta completamente.', True)
    confirmacion = confirmar_accion('¿Desea eliminar esta receta?')
    
    if not confirmacion:
        return
    
    respuesta = 'La receta se ha eliminado exitosamente.'
    print(respuesta)
    continuar()


def ir_a_eliminar_categoria():
    limpiar_consola()
    mostrar_alerta('Se eliminará esta categoría y todo su contenido.', True)
    confirmacion = confirmar_accion('¿Desea eliminar esta categoría?')

    if not confirmacion:
        return
    
    respuesta = 'La categoría se ha eliminado exitosamente.'
    print(respuesta)
    continuar()


########################### SCRIPT PRINCIPAL ###########################
    
def ejecutar_programa(directorio_base):
    '''
    La columna vertebral del proyecto.
    
    Idealmente, ésta debería ser llamada por medio del
    infame if __name__ == '__main__', pero a fin de
    evitar posibles conflictos con otros proyectos
    del cwd, mejor la dejo como está. 🤷‍♂️
    '''
    mostrar_introduccion(directorio_base)
    salir = False

    while not salir:
        mostrar_menu_principal()
        opcion = escoger_opcion()

        if opcion == 1:
            ir_a_leer_receta(directorio_base)
        elif opcion == 2:
            ir_a_crear_receta(directorio_base)
        elif opcion == 3:
            ir_a_crear_categoria()
        elif opcion == 4:
            ir_a_eliminar_receta()
        elif opcion == 5:
            ir_a_eliminar_categoria()
        elif opcion == 6:
            salir = confirmar_accion('¿Desea salir?')
        else:
            mostrar_error(f'La opción "{opcion}" no es válida.')


ejecutar_programa(DIRECTORIO_BASE)
