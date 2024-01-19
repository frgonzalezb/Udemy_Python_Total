mi_lista = ['a', 'b', 'c']
print(type(mi_lista))

otra_lista = ['a', 10, 6.3]
print(type(mi_lista))

nueva_lista = ['d', 'e', 'f']
print(mi_lista + nueva_lista)

lista_desordenada = ['g', 'd', 'f', 'e', 'z', 't']
lista_desordenada.sort()
print(lista_desordenada) # Devuelve la lista en orden alfabético
lista_desordenada.reverse()
print(lista_desordenada) # Devuelve la lista en orden alfabético en reversa
