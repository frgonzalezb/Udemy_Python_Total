'''
Escribe una función llamada contar_primos() que requiera un 
solo argumento numérico.

Esta función va a mostrar en pantalla todos los números 
primos existentes en el rango que va desde cero hasta ese 
número incluido, y va a devolver la cantidad de números 
primos que encontró.

Aclaración, por convención el 0 y el 1 no se consideran primos.
'''
import math


# NOTA DEV: Utilicé el teorema de Wilson como base de mi solución
def contar_primos(n):
    lista_primos = []
    
    for i in range(0, n+1):
        if i > 1 and (math.factorial(i-1) + 1) % i == 0:
            lista_primos.append(i)

    print(lista_primos)

    return len(lista_primos)
    

print(contar_primos(1000))


'''
# NOTA SOLUCIÓN PROFE:
# Se puede hacer sin módulos adicionales de la siguiente forma:

def contar_primos(numero):
    primos = [2]
    iteracion = 3
    if numero < 2:
        return 0
    while iteracion <= numero:
        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)
'''
