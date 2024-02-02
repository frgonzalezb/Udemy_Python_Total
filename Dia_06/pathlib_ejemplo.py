import os
from pathlib import Path, PureWindowsPath


cwd = os.getcwd().replace('\\', '/')
ruta = Path(cwd + '/Dia_06' + '/Prueba.txt')

print(ruta.read_text()) # Devuelve el contenido
print(ruta.name)        # Devuelve el nombre completo del archivo
print(ruta.stem)        # Devuelve solo la parte nombre
print(ruta.suffix)      # Devuelve solo la parte extension

if not ruta.exists():
    print('Este archivo no existe.')

ruta_windows = PureWindowsPath(ruta)
print(ruta_windows)
