'''
Medir tiempo de ejecución y eficiencia.
'''


import time
import timeit


def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


'''
# Pruebas usando módulo time
inicio = time.time()
prueba_for(100000)
final = time.time()
print(f'prueba_for:   {final - inicio} s')

inicio = time.time()
prueba_while(100000)
final = time.time()
print(f'prueba_while: {final - inicio} s')
'''


# Pruebas usando módulo timeit
declaracion_1 = '''
prueba_for(10)
'''

declaracion_2 = '''
prueba_while(10)
'''

mi_setup_1 = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

mi_setup_2 = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

n = 100000
duracion_1 = timeit.timeit(declaracion_1, mi_setup_1, number=n)
duracion_2 = timeit.timeit(declaracion_2, mi_setup_2, number=n)
print(type(duracion_1))
print(f'La duración de repetir {n} veces {declaracion_1} es {duracion_1} s.')
print(f'La duración de repetir {n} veces {declaracion_2} es {duracion_2} s.')
