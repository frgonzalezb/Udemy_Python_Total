def es_entero_de_3_cifras(numero):
    return int(numero) in range(100, 1000)


def chequear_lista_numero_3_cifras(lista):
    lista_3_cifras = []

    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append(n)

    return lista_3_cifras

resultado = chequear_lista_numero_3_cifras([555, 99, 666, 7777])
print(resultado)
