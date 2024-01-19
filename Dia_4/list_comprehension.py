# Sin comprehensión de listas
palabra = 'python'
lista = []

for letra in palabra:
    lista.append(letra)

print(lista)


# Con comprehension de listas
palabra = 'python'
lista = [letra for letra in palabra]
'''
Parafraseando al profe:
Añade a 'lista' una 'letra' por cada 'letra' en 'palabra'.
El primer 'letra' sería como el 'lista.append(letra)'.
'''
print(lista)


# Otro ejemplo usando números y condicional if
lista = [n for n in range(0, 21, 2) if n * 2 > 10]
print(lista)

# Para añadir else, hay que invertir el orden
lista = [n if n * 2 > 10 else 'no' for n in range(0, 21, 2)]
print(lista)

# Conversor de pies a metros
pies = [10, 20, 30, 40, 50]
metros = [round(p / 3.281, 2) for p in pies]
print(metros)

# Conversor grados °F a °C
temp_fahrenheit = [32, 212, 275]
grados_celsius = [(temp-32)*(5/9) for temp in temp_fahrenheit]
print(grados_celsius)
