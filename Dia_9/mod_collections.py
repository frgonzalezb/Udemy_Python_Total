'''
Explorando el módulo collections.
'''


from collections import Counter, defaultdict, namedtuple, deque


numeros = [0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 3]
print(Counter(numeros))         # Counter({1: 5, 2: 3, 0: 2, 3: 1})
print(type(Counter(numeros)))   # <class 'collections.Counter'>

palabra = 'Mississippi'
print(Counter(palabra))         # Counter({'i': 4, 's': 4, 'p': 2, 'M': 1})

frase = 'al pan pan y al vino vino'
print(Counter(frase.split()))   # Counter({'al': 2, 'pan': 2, 'vino': 2, 'y': 1})

serie = Counter(numeros)
print(serie.most_common())      # [(1, 5), (2, 3), (0, 2), (3, 1)]
print(serie.most_common(1))     # [(1, 5)]
print(serie.most_common(2))     # [(1, 5), (2, 3)]
print(list(serie))              # [0, 1, 2, 3]


'''
mi_dic = {
    'uno': 'rojo',
    'dos': 'verde',
    'tres': 'azul'
}

print(mi_dic['cuatro'])     # Levantará error
'''

mi_dic = defaultdict(lambda: 'nada')
mi_dic['uno'] = 'rojo'
print(type(mi_dic))     # <class 'collections.defaultdict'>
print(mi_dic)           # defaultdict(<function <lambda> at ...>, {'uno': 'rojo'})
print(mi_dic['dos'])    # nada


'''
mi_tupla = (500, 18, 65)
print(mi_tupla[1])
'''

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 69)
print(type(ariel))      # <class '__main__.Persona'>
print(ariel.altura)     # 1.76
print(ariel.peso)       # 69
print(ariel[2])         # 69


'''
Una cola doblemente terminada o deque (del inglés double ended queue) 
es una estructura de datos lineal que permite insertar y eliminar 
elementos por ambos extremos.
'''

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(type(lista_ciudades))
lista_ciudades.append('Santiago')
lista_ciudades.appendleft('Buenos Aires')
print(lista_ciudades)
