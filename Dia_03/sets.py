mi_set = set([1, 2, 3, 4, 5])
print(mi_set)
print(type(mi_set))

otro_set = {1, 2, 3}
print(otro_set)
print(type(otro_set))

# Python automáticamente reconoce el set y elimina los valores duplicados
nuevo_set = set([1, 2, 3, 4, 5, 1, 1, 1, 2, 2, 2])
print(nuevo_set)

# Sets no admiten listas ni diccionarios, pero sí tuplas (inmutables)
tupla_set = set([1, 2, 3, (1, 2, 3)])
print(tupla_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)

set1.add(4) # Si es duplicado, simplemente no lo agrega
print(set1)

set1.remove(4) # Si no existe, levanta error
print(set1)

set1.discard(4) # Si no existe, simplemente no pasa nada
print(set1)

set1.clear() # Deja el set vacío
print(set1)
