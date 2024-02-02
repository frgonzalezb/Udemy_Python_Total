def reducir_lista(lista):
    lista.sort()

    for elemento in lista:
        if lista.count(elemento) > 1:
            lista.pop(lista.index(elemento))
    
    lista.remove(max(lista))
    
    return lista


def promedio(lista):
    sumatoria = 0
    largo_lista = len(lista)

    for n in lista:
        sumatoria += n

    return sumatoria / largo_lista
    

lista_numeros = [1, 2, 15, 7, 2]
lista_reducida = reducir_lista(lista_numeros)
