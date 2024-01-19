'''
Uso de índices y función index() en cadenas.
'''

texto = 'Esta es una prueba'

resultado = texto[0]
print(resultado) # Imprime 'E'

resultado = texto[6]
print(resultado) # Imprime 's'

resultado = texto[-6]
print(resultado) # Imprime 'p'

resultado = texto.index('t')
print(resultado) # Imprime '2' (el índice de la primera letra 't' encontrada)

resultado = texto.index('prueba')
print(resultado) # Imprime '12' (el índice donde comienza la palabra 'prueba')

resultado = texto.index('a', 5)
print(resultado) # Imprime '10', que es la primera 'a' desde el index 5

'''
resultado = texto.index('a', 5, 10)
print(resultado) # ValueError: substring not found
# Intenta imprimir la 'a' del index 10, pero el valor final no es inclusivo
# (Similar a lo que ocurre en range() del ciclo for)
'''

resultado = texto.rindex('a') # rindex() busca de derecha a izquierda
print(resultado) # Imprime '17'
