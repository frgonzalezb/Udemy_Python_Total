def hr(character='-', length=80, pre_margin=False, post_margin=False):
    '''
    Simple low-cost <hr> tag for console.
    '''
    rule = character * length
    margin = '\n'

    if pre_margin:
        print(margin + rule)
    elif post_margin:
        print(rule + margin)
    elif pre_margin and post_margin:
        print(margin + rule + margin)
    else:
        print(rule)


def obtener_lista(lista):
    ultimo = len(lista)

    for nombre in lista:
        lugar = lista.index(nombre) + 1
        saludo = f'¡Hola, {nombre}!\nTu lugar en la lista es {lugar}.\n'

        if lugar == 1:
            saludo = saludo + 'Eres el primero en la lista, ¡felicitaciones!\n'
        if lugar == ultimo:
            saludo = saludo + 'Eres el último en la lista, ¡ánimo!\n'
        
        print(saludo)

nombres = ['Juan', 'Ana', 'Carlos', 'Belén', 'Nico', 'María', 'Paco', 'Fran']
obtener_lista(nombres)

hr()

numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    print(f'{mi_valor} + {numero} = {mi_valor + numero}')
    mi_valor = mi_valor + numero

print(f'Total = {mi_valor}\n')

hr()

cadena = input('Ingresa una palabra o frase: ')

for caracter in cadena:
    print(caracter.upper())

hr()

for objeto in [[1, 2], [3, 4], [5, 6]]:
    print(objeto)

hr()

for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)

hr()

for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)

hr()

nombre = input('Ingresa tu nombre: ')
edad = input('Ingresa tu edad: ')
ocupacion = input('Ingresa tu ocupación: ')

d = {
    'nombre': nombre, 
    'edad': edad,
    'ocupacion': ocupacion
}

print('\nPares de clave-valor:')
for k, v in d.items():
    print(f'{k}: {v}')

print('\nSólo claves:')
for k in d.keys():
    print(k)

print('\nSólo valores:')
for v in d.values():
    print(v)
