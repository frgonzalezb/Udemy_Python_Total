'''
Crea una función llamada abrir_leer() que abra (open) un archivo 
indicado como parámetro, y devuelva su contenido (read).
'''

def abrir_leer(archivo):
    leer = open(archivo)
    return leer.read()


'''
Crea una función llamada sobrescribir() que abra (open) un archivo 
indicado como parámetro, y sobrescriba cualquier contenido anterior 
por el texto "contenido eliminado"
'''

def sobrescribir(archivo):
    file = open(archivo, 'w')
    return file.write("contenido eliminado")


'''
Crea una función llamada registro_error() que abra (open) un archivo 
indicado como parámetro, y lo actualice añadiendo una línea al final 
que indique "se ha registrado un error de ejecución". Finalmente, 
debe cerrar el archivo abierto.
'''

def registro_error(archivo):
    log = open(archivo, 'a')
    log.write("se ha registrado un error de ejecución")
    log.close()
