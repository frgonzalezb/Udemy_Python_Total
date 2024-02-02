'''
Crea una función llamada devolver_distintos() 
que reciba 3 integers como parámetros.

Si la suma de los 3 numeros es mayor a 15, 
va a devolver el número mayor.

Si la suma de los 3 numeros es menor a 10, 
va a devolver el número menor.

Si la suma de los 3 números es un valor entre 10 y 15 (incluidos), 
va a devolver el número de valor intermedio.
'''

def devolver_distintos(int1, int2, int3):
    lista = [int1, int2, int3]

    if (int1 + int2 + int3) > 15:
        return max(lista)
    elif (int1 + int2 + int3) < 10:
        return min(lista)
    else:
        lista.remove(min(lista))
        lista.remove(max(lista))
        return lista[0]


print(devolver_distintos(1, 2, 3)) # 1
print(devolver_distintos(4, 5, 6)) # 5
print(devolver_distintos(7, 8, 9)) # 9


# NOTA SOLUCIÓN PROFE:
# Para el else, también puede usarse lista.sort() y luego devolver lista[1]
