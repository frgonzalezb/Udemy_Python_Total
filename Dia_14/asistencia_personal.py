'''
IDEA DEL PROYECTO (según el profe):

Sistema que, mediante ena webcam en vivo, permite verificar y registrar la 
asistencia de un trabajador por reconocimiento facial, efectuando una 
comparación de las tomas con imágenes almacenadas en una base de datos.
'''


import os
import cv2
import face_recognition as fr
import numpy as np

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

# Tomar imagen de webcam
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Leer la imagen de la camara
exito, imagen = captura.read()

if not exito:
    print('No se ha podido tomar la captura.')
    exit()

# Reconocer cara en captura
cara_captura = fr.face_locations(imagen)

# Codificar cara capturada
cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

# Buscar coincidencias
for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
    coincidencia = fr.compare_faces(lista_empleados_codificada, caracodif)
    distancias = fr.face_distance(lista_empleados_codificada, caracodif)
    print(distancias) # dbg

    indice_coincidencia = np.argmin(distancias)

    # Mostrar coincidencias
    if distancias[indice_coincidencia] > 0.6:
        print('Su rostro no coincide con ninguno de nuestros empleados.')
        exit()
    
    print('Bienvenido a su nueva jornada.') # dbg

    # Buscar el nombre del emplado encontrado
    nombre = nombres_empleados[indice_coincidencia]

    y1, x2, y2, x1 = caraubic
    cv2.rectangle(
        imagen, 
        (x1, y1), 
        (x2, y2), 
        (0, 255, 0), 
        2
    )
    cv2.rectangle(
        imagen, 
        (x1, y2 - 35), 
        (x2, y2), 
        (0, 255, 0), 
        cv2.FILLED
    )
    cv2.putText(
        imagen, 
        nombre, 
        (x1 + 6, y2 - 6), 
        cv2.FONT_HERSHEY_COMPLEX, 
        1, 
        (255, 255, 255), 
        2
    )

    # Mostrar imagen obtenida
    cv2.imshow('Imagen web', imagen)

    # Mantener ventana abierta
    cv2.waitKey(0)
