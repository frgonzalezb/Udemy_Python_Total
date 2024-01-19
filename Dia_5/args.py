def obtener_sumatoria(*args):
    return sum(args)


def suma_cuadrados(*args):
    return sum(arg ** 2 for arg in args)


def suma_absolutos(*args):
    return sum(abs(arg) for arg in args)


def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'


print(obtener_sumatoria(5, 6, 4, 2))
print(suma_cuadrados(1,2,3))
print(suma_absolutos(-1,2,-3))
print(numeros_persona(input('Tu nombre: '), 2, 3, 4, 5))
