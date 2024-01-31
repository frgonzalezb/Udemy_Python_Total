import os
import re
import time

from colored import Fore, Style
from datetime import date
from pathlib import Path


# Colores
RED = Fore.red
YELLOW = Fore.yellow
GREEN = Fore.green
BLUE = Fore.blue
MAGENTA = Fore.magenta
RESET = Style.reset

ROOT = Path(os.getcwd(), 'Dia_9', 'Proyecto', 'Mi_Gran_Directorio')
PATTERN = r'N\w{3}-\d{5}'


def generar_hr(str_o_int):
    if type(str_o_int) is int:
        return '-' * str_o_int
    return '-' * len(str_o_int)


def obtener_fecha_busqueda():
    return f'{YELLOW}Fecha de búsqueda:{RESET} {date.today().strftime('%d-%m-%Y')}\n'


def generar_encabezados(palabras: list):
    titulos = '\t\t'.join(palabras).upper()
    subrayado = '\t\t'.join([generar_hr(palabras[0]), generar_hr(palabras[1])])
    return (titulos, subrayado)


def recorrer_directorio(ruta):
    archivos_detectados = []
    patrones_detectados = []

    for carpeta, _, archivos in ruta:
        if archivos:
            for archivo in archivos:
                path = Path(carpeta, archivo)
                revision = open(path, 'r')
                busqueda = re.search(PATTERN, revision.read())
                if busqueda:
                    archivos_detectados.append(archivo)
                    patrones_detectados.append(busqueda.group())
                revision.close()

    return dict(zip(archivos_detectados, patrones_detectados))


def enmarcar_informe(funcion):
    def informe():
        linea = f'{RED}{generar_hr(52)}{RESET}'
        print(linea)
        funcion()
        print(linea)
    return informe


@enmarcar_informe
def buscar_nro_serie():
    print(obtener_fecha_busqueda())

    titulos, subrayado = generar_encabezados(['archivo', 'nro. serie'])
    print(GREEN + titulos + '\n' + BLUE + subrayado + RESET)

    inicio = time.time()
    resultados = recorrer_directorio(os.walk(ROOT))

    for archivo, serie in resultados.items():
        print(f'{archivo}\t{serie}')
    final = time.time()

    print(f'\n{BLUE}Números encontrados:{RESET} {len(resultados.keys())}')
    print(f'{MAGENTA}Duración de la búsqueda:{RESET} {round(final - inicio, 3)} s')


# Usage
buscar_nro_serie()
