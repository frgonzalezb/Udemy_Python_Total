'''
Uso de módulo re para expresiones regulares.

CAR     DESCRIPCIÓN         EJEMPLO
\d  =   numérico        =   v\d.\d\d        # v1.00 o v2.95
\w  =   alfanumérico    =   \w\w\w-\w\w     # sol-do o ABC-25
\s  =   whitespace      =   núm\s\d\d       # núm 07 o núm 69
\D  =   NO numérico     =   \D\D\D\D        # abcd o ABC?
\W  =   NO alfanumérico =   \W\W\W          # ??? o ###
\S  =   NO whitespace   =   \S\S\S\S        # 1234 o abcd

CUANTIFICADORES:
CAR{n}      Encontrar o repetir CAR de n veces
CAR+        Encontrar o repetir CAR de 1 o más veces
CAR{n, m}   Encontrar o repetir CAR de n a m veces
CAR{n, }    Encontrar o repetir CAR de n a más veces
CAR*        Encontrar o repetir CAR de 0 o más veces
CAR?        Encontrar o repetir CAR de 0 o 1 vez
'''


import re


# Patrón para ###-###-####
PATRON_1 = r'\d\d\d-\d\d\d-\d\d\d\d'
PATRON_2 = r'\d{3}-\d{3}-\d{4}'    # PATRON_1 con cuantificadores


def validate_phone_1(phone):
    return True if re.match(PATRON_1, phone) else False


def validate_phone_2(phone):
    return True if re.match(PATRON_2, phone) else False


print(validate_phone_1('333-333-3333'))   # True
print(validate_phone_1('333-333-333f'))   # False

print(validate_phone_2('333-333-3333'))   # True
print(validate_phone_2('333-333-333f'))   # False


# Ejemplo con texto y patrón concreto
texto = 'Si necesitas ayuda, llama al (658)-598-9977 las 24 horas al servicio de ayuda online.'
palabra = 'ayuda' in texto
print(palabra)  # True

patron = 'nada' # Un patrón puede ser concreto como una palabra natural

busqueda = re.search(patron, texto)
print(busqueda) # None

busqueda = re.search('ayuda', texto)
print(busqueda)         # <re.Match object; span=(13, 18), match='ayuda'>
print(busqueda.span())  # (13, 18)
print(busqueda.start()) # 13
print(busqueda.end())   # 18

busqueda = re.findall('ayuda', texto)
print(busqueda)         # ['ayuda', 'ayuda']
print(type(busqueda))   # <class 'list'>

for hallazgo in re.finditer('ayuda', texto):
    print(hallazgo.span())  # (13, 18) y (72, 77)


# Otro ejemplo con texto y patrón abstracto
texto = 'llama al 564-525-6588 ya mismo'
patron = r'\d{3}-\d{3}-\d{4}' # Un patrón también puede ser abstracto

busqueda = re.search(patron, texto)
print(busqueda)         # <re.Match object; span=(9, 21), match='564-525-6588'>
print(busqueda.group()) # 564-525-6588

patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
busqueda = re.search(patron, texto)
print(busqueda.group())     # 564-525-6588
print(busqueda.group(1))    # 564
print(busqueda.group(2))    # 525
print(busqueda.group(3))    # 6588


# Ejemplo interactivo: creación de clave
clave = input('Invente una clave: ')
patron = r'\D{1}\w{7}'
chequear = re.search(patron, clave)
print(chequear) # None si no se encuentra el patrón


# Más trucos
texto = 'No atendemos los lunes por la tarde'
buscar = re.search(r'lunes|martes', texto)  # Buscar 'lunes' o 'martes'
print(buscar)   # <re.Match object; span=(18, 23), match='lunes'>

texto = 'No atendemos los jueves por la tarde'
buscar = re.search(r'lunes|martes', texto)  # Buscar 'lunes' o 'martes'
print(buscar)   # None

buscar = re.search(r'demos', texto)
print(buscar)   # <re.Match object; span=(7, 12), match='demos'>

buscar = re.search(r'.demos', texto)
print(buscar)   # <re.Match object; span=(6, 12), match='ndemos'>

buscar = re.search(r'....demos', texto)
print(buscar)   # <re.Match object; span=(3, 12), match='atendemos'>

buscar = re.search(r'....demos....', texto)
print(buscar)   # <re.Match object; span=(3, 16), match='atendemos los'>

buscar = re.search(r'^\d', texto) # ^ = Si patrón en el comienzo del string
print(buscar)   # None

buscar = re.search(r'^\D', texto)
print(buscar)   # <re.Match object; span=(0, 1), match='N'>

buscar = re.search(r'\d$', texto) # $ = Si patrón al final del string
print(buscar)   # None

buscar = re.search(r'\D$', texto)
print(buscar)   # <re.Match object; span=(35, 36), match='e'>

buscar = re.findall(r'[^\s]', texto) # [^] = Excluir del patrón
print(buscar)   # Todos los caracteres de texto, menos los espacios

buscar = re.findall(r'[^\s]+', texto)
print(buscar)           # ['No', 'atendemos', 'los', 'jueves', 'por', 'la', 'tarde']
print(''.join(buscar))  # Noatendemoslosjuevesporlatarde
