# Con ruta relativa por el entorno virtual 😑
ruta_relativa = './Dia_6/'
mi_archivo = open(ruta_relativa + 'Prueba.txt')

'''
# Leer el contenido abierto
print(mi_archivo)           # Propiedades del archivo
print(mi_archivo.read())    # El contenido del archivo
'''

'''
# Leer solo una línea por vez (se debe omitir read())
una_linea = mi_archivo.readline()   # Primera
print(una_linea.upper())            # Se pueden aplicar métodos str
una_linea = mi_archivo.readline()   # Segunda
print(una_linea.rstrip())           # Borrar salto de línea implícito
una_linea = mi_archivo.readline()   # Tercera
print(una_linea)
'''

'''
# Recorrer el contenido del archivo
for linea in mi_archivo:
    print('Aquí dice ' + linea)
'''

'''
# Capturar líneas como lista
todas = mi_archivo.readlines()
print(todas)
todas.pop()     # Se pueden usar métodos de lista
print(todas)    # Se eliminó la última línea
'''

# Imprime solamente la segunda línea
lista = list(enumerate(mi_archivo.readlines()))

for i, linea in lista:
    if i == 1:
        print(linea)

mi_archivo.close()
