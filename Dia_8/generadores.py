def mi_funcion():
    return 4


def mi_generador():
    yield 4


print(mi_funcion())     # 4
print(mi_generador())   # <generator object mi_generador at ...>

generador = mi_generador()
print(next(generador))  # 4


'''
Usar generadores es más económico no sólo en términos de líneas escritas, 
sino también en términos de uso de recursos (principalmente, memoria).
'''


def nueva_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista


def nuevo_generador():
    for x in range(1, 5):
        yield x * 10


print(nueva_funcion())      # [10, 20, 30, 40]
print(nuevo_generador())    # <generator object nuevo_generador at ...>

generador = nuevo_generador()
print(next(generador))      # 10
print(next(generador))      # 20
print(next(generador))      # 30
print(next(generador))      # 40
# print(next(generador))      # Error StopIteration


'''
A diferencia de "return" en una función, se pueden colocar tantos "yield" 
como sean necesarios en un generador.
'''


def cool_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


g = cool_generador()

print(next(g))
print(next(g))
print('No importa si hay código aquí, el generador recordará su posición.')
print(next(g))
