import os
from pathlib import Path


# Get current working directory
ruta = os.getcwd()
print(ruta)

'''
# Change directory
otra_ruta = os.chdir(input('Ingrese directorio: '))

# Abrir archivo en ese directorio
archivo = open(input('Ingrese nombre de archivo y extension: '))
print('Contenido en archivo: ' + archivo.read())
archivo.close()
'''

# Crear directorio
os.makedirs(ruta + '\\Dia_6\\mkdirs_test')

# Eliminar directorio
os.rmdir(ruta + '\\Dia_6\\mkdirs_test')


# Obtener partes de la ruta
elemento = os.path.basename(ruta + '\\Dia_6\\Prueba.txt')
print(elemento)
elemento = os.path.dirname(ruta + '\\Dia_6\\Prueba.txt')
print(elemento)
elemento = os.path.split(ruta + '\\Dia_6\\Prueba.txt')
print(elemento)


# Lo anterior funciona ok con Windows, pero no en otros OS
# A veces, mejor usar Path
ruta = ruta + '\\Dia_6'
carpeta = Path(ruta.replace('\\', '/'))
archivo = carpeta / 'Prueba.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())
