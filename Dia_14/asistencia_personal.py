'''
IDEA DEL PROYECTO (según el profe):

Sistema que, mediante ena webcam en vivo, permite verificar y registrar la 
asistencia de un trabajador por reconocimiento facial, efectuando una 
comparación de las tomas con imágenes almacenadas en una base de datos.
'''


import os
import cv2
import face_recognition as fr
from pathlib import Path


CWD = os.getcwd()

# Crear base de datos
ruta = Path(CWD, 'Files', 'Empleados')
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)
print(lista_empleados) # dbg

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)

# Codificar imágenes
def codificar(imagenes):
    # Crear lista nueva
    lista_codificada = []

    # Pasar imagenes a RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # Codificar
        codificado = fr.face_encodings(imagen)[0]

        # Agregar a lista
        lista_codificada.append(codificado)

    # Devolver lista codificada
    return lista_codificada


lista_empleados_codificada = codificar(mis_imagenes)
print(lista_empleados_codificada)
