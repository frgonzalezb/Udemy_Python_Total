from random import randint, uniform, random, choice, shuffle


aleatorio = randint(1, 50)
print(aleatorio)

aleatorio = round(uniform(1, 5), 2)
print(aleatorio)

aleatorio = round(random(), 2)
print(aleatorio)

colores = ['azul', 'rojo', 'verde', 'amarillo']

aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5, 51, 5))
print(f'Lista original: {numeros}')
shuffle(numeros)
print(f'Lista shuffle: {numeros}')