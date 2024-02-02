'''
CONSIGNA:

-   El usuario debe ingresar un texto cualquiera.
-   El usuario debe ingresar 3 letras diferentes a su elección.
-   El programa devuelve al usuario 5 tipos de análisis:

    1. Mostrar cuántas veces aparece cada letra que eligió.
        Tip: Almacenar letras en una lista.
    2. Mostrar cuántas palabras hay en total en el texto.
        Tip: Transformar texto en lista de palabras y calcular longitud.
    3. Mostrar la primera y última letra del texto.
    4. Mostrar el texto en orden inverso.
    5. Verificar si aparece la palabra 'Python' en el texto.
'''

# El usuario debe ingresar un texto cualquiera
texto = input(
    'Ingrese algún texto cualquiera (cuento, poema, etc.): '
)

# El usuario debe ingresar 3 letras diferentes a su elección
letras = input(
    'Ingrese 3 letras diferentes cualesquiera, separadas por espacios (e.g. A B C): '
)


# PROCESAMIENTO

# Transformar texto y letras a minúsculas
texto = texto.lower()
letras = letras.lower()


# PROPIO: Eliminar puntos y comas para un resultado más limpio
if '.' in texto:
    texto = texto.replace('.', '')

if ',' in texto:
    texto.replace(',', '')
# PD: Sí, ya sé que con regex sería más eficiente, pero aquí da igual


# ANÁLISIS 1. Mostrar cuántas veces aparece cada letra que eligió
lista_letras = letras.split()

# Separar las letras
letra_lista_1 = lista_letras[0]
letra_lista_2 = lista_letras[1]
letra_lista_3 = lista_letras[2]

# Contar ocurrencia de cada letra en el texto
contar_letra_1 = texto.count(letra_lista_1)
contar_letra_2 = texto.count(letra_lista_2)
contar_letra_3 = texto.count(letra_lista_3)

# Devolver la respuesta
analisis_1 = f'''
    ANÁLISIS 1:
    - La letra "{letra_lista_1.upper()}" aparece {contar_letra_1} veces.
    - La letra "{letra_lista_2.upper()}" aparece {contar_letra_2} veces.
    - La letra "{letra_lista_3.upper()}" aparece {contar_letra_3} veces.
'''
print(analisis_1)

# ANÁLISIS 2. Mostrar cuántas palabras hay en total en el texto
lista_texto = texto.split()
cuenta_palabras_texto = len(lista_texto)

analisis_2 = f'''
    ANÁLISIS 2:
    El texto ingresado contiene {cuenta_palabras_texto} palabras en total.
'''
print(analisis_2)

# ANÁLISIS 3. Mostrar la primera y última letra del texto
primera_letra = texto[0]
ultima_letra = texto[-1]

analisis_3 = f'''
    ANÁLISIS 3:
    - La primera letra del texto ingresado es "{primera_letra.upper()}".
    - La última letra del texto ingresado es "{ultima_letra.upper()}".
'''
print(analisis_3)

# ANÁLISIS 4. Mostrar el texto en orden inverso
lista_texto.reverse()
texto_invertido = ' '.join(lista_texto)

analisis_4 = f'''
    ANÁLISIS 4:
    El texto ingresado en orden invertido:
    "{texto_invertido}"
'''
print(analisis_4)

# ANÁLISIS 5. Verificar si aparece la palabra 'Python' en el texto
python_en_texto = 'python' in texto

analisis_5 = f'''
    ANÁLISIS 5:
    ¿Aparece "Python" en el texto? (True o False): {python_en_texto}
'''
print(analisis_5)
