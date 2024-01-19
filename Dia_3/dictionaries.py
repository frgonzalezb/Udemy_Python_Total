diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(diccionario)
print(type(diccionario))

valor = diccionario['c1']
print(f'El valor de de la clave "c1" es {valor}')

cliente = {
    'nombre': 'Juan',
    'apellido': 'Fuentes',
    'peso': 88,
    'talla': 1.76
}

consulta = cliente['apellido']
print(consulta)

dict = {
    'c1': 55,
    'c2': [10, 20, 30],
    'c3': {'s1': 100, 's2': 200}
}

print(f'Lo que hay en el índice 1 de "c2" es {dict['c2'][1]} ')
print(f'Lo que hay en la clave "s2" de "c3" es {dict['c3']['s2']}')

letters = {
    'c1': ['a', 'b', 'c'],
    'c2': ['d', 'e', 'f']
}

print(letters['c2'][1].upper())

new_dict = {1: 'a', 2: 'b'}
print(new_dict)
new_dict[3] = 'c'           # Equivale a append en diccionarios
print(new_dict)
new_dict[2] = 'B'           # Sobreescribe valor
print(new_dict)
print(new_dict.keys())      # Devuelve solo las claves
print(new_dict.values())    # Devuelve solo los valores
print(new_dict.items())     # Devuelve todos los items
