texto = 'Este es el texto de Federico'

resultado = texto.upper()
print(resultado)            # Imprime texto en mayúsculas

resultado = texto.lower()
print(resultado)            # Imprime texto en minúsculas

resultado = texto.split()
print(resultado)            # Imprime texto como lista

resultado = texto.split('t')
print(resultado)            # Idem, pero toma 't' como separador

lista = ['Aprender', 'Python', 'es', 'genial']

resultado = ' '.join(lista)
print(resultado)            # Imprime lista como cadena

resultado = texto.find('s')
print(resultado)            # Imprime '1' (index)

resultado = texto.find('g')
print(resultado)            # Imprime '-1' (equivale a 404 de html)

resultado = texto.replace('Federico', 'todes')
print(resultado)            # Imprime 'Este es el texto de todes'

resultado = texto.replace('e', 'x')
print(resultado)            # Imprime 'Estx xs xl txxto dx Fxdxrico'
