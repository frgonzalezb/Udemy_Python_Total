import os
import cv2
import face_recognition as fr

from pathlib import Path


CWD = os.getcwd()


# Cargar imágenes
archivo_control = Path(CWD, 'Files', 'FotoA.jpg')
archivo_prueba = Path(CWD, 'Files', 'FotoB.jpg')
foto_control = fr.load_image_file(archivo_control)
foto_prueba = fr.load_image_file(archivo_prueba)

# Pasar imágenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

print(lugar_cara_A) # Coordenadas CSS (top, right, bottom, left)

# Localizar cara prueba
lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

print(lugar_cara_B) # Coordenadas CSS (top, right, bottom, left)

# Mostrar rectángulo
cv2.rectangle(
    foto_control, 
    (lugar_cara_A[3], lugar_cara_A[0]),
    (lugar_cara_A[1], lugar_cara_A[2]),
    (0, 255, 0),
    2
)
cv2.rectangle(
    foto_prueba, 
    (lugar_cara_B[3], lugar_cara_B[0]),
    (lugar_cara_B[1], lugar_cara_B[2]),
    (0, 255, 0),
    2
)

# Mostrar imágenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

# Mantener programa abierto
cv2.waitKey(0)
