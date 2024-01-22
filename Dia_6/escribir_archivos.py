'''
GLOSARIO Modos de apertura en open()

r = sólo lectura (modo por defecto)
w = sólo escritura (archivo se sobrescribe completo, o sea crea si no existe)
a = sólo escritura (cursor al final del archivo, se mantiene contenido previo; 
    se crea archivo nuevo si no existe)
'''

# Con ruta relativa por el entorno virtual 😑
ruta_relativa = './Dia_6/'

'''
# Con 'r' explícito
archivo = open(ruta_relativa + 'Prueba.txt', 'r')
archivo.write('Soy el nuevo texto') # No lo deja sobrescribir
archivo.close()
'''

# Nuevo archivo con 'w'
archivo = open(ruta_relativa + 'prueba1.txt', 'w')
archivo.write('Soy el nuevo texto')
archivo.close()

# Sobrescribir todo el contenido del nuevo archivo
archivo = open(ruta_relativa + 'prueba1.txt', 'w')
archivo.write('¡NO!\nYo soy el nuevo texto')
archivo.close()

# Sobrescribir con cadenas de una lista
archivo = open(ruta_relativa + 'prueba1.txt', 'w')
archivo.writelines(['Primera línea\n', 'Segunda línea'])
archivo.close()

# Sobrescribir con varias líneas, the right way
archivo = open(ruta_relativa + 'prueba1.txt', 'w')
lista = ['Primera', 'Segunda', 'Tercera', 'Cuarta', 'Quinta']
for palabra in lista:
    archivo.writelines(palabra + '\n')
archivo.close()

# Agregar contenido sin sobrescribir (p.e. logs)
archivo = open(ruta_relativa + 'prueba1.txt', 'a')
archivo.write('Nuevo contenido!!!\n')
archivo.close()
