'''
Uso de módulos os y shutil.

NOTAS IMPORTANTES:
-   Evitar usar shutil.rmtree() ya que borra todo el contenido de una
    ruta y sus subdirectorios completamente y de forma irreversible, 
    sin enviarlos a la papelera de reciclaje.
-   Para eliminar archivos de forma segura, se recomienda usar alguna
    herramienta como Send2Trash.
    -   pip install Send2Trash
    -   send2trash.send2trash('ruta/al/archivo')
'''


import os
import send2trash

import utilidades
from utilidades import RED, YELLOW, RESET


archivo = open('borrame_pls.txt', 'w')
archivo.close()

print('Archivo borrame_pls.txt creado en la carpeta raíz del cwd.')
utilidades.esperar_usuario()

send2trash.send2trash('borrame_pls.txt')
print('Archivo borrame_pls.txt enviado a la papelera.')

ruta = os.getcwd() + '\\Dia_08'

for carpeta, subcarpetas, archivos in os.walk(ruta):
    print(f'{YELLOW}CARPETA: {carpeta}{RESET}')
    
    if len(subcarpetas) == 0:
        print(f'\t{RED}No hay subcarpetas.{RESET}')
    else:
        print('\tLas subcarpetas son: ')
        for subcarpeta in subcarpetas:
            print(f'\t\t{subcarpeta}')
    
    if len(archivos) == 0:
        print(f'\t{RED}No hay archivos.{RESET}')
    else:
        print('\tLos archivos son: ')
        for archivo in archivos:
            print(f'\t\t{archivo}')
    print('\n')
