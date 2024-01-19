lista = ['a', 'b', 'c']

for item in enumerate(lista):
    print(item)

for index, item in enumerate(lista):
    print(index, item)

for index, item in enumerate(range(50, 55)):
    print(index, item)

mis_tuplas = list(enumerate(lista))
print(mis_tuplas)

# ------------------------------------------------------------------------------
'''
Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:

Loops

Condicionales if

El método enumerate()

Métodos de strings o indexado
'''

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
tupla_nombres = list(enumerate(lista_nombres))

for index, element in tupla_nombres:
    if element.startswith('M'):
        print(index)
