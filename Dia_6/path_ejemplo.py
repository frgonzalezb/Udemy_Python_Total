from pathlib import Path


# Crear de rutas relativas
guia = Path('Barcelona', 'Sagrada_Familia.txt') 
print(guia) # Barcelona\Sagrada_Familia.txt


# Saber la ruta 'home' del usuario del sistema
base = Path.home()
print(base) # C:\Users\<tu-usuario>


# Crear una ruta absoluta con objetos Path y cadenas
guia = Path(base, 'Barcelona', 'Sagrada_Familia.txt')
print(guia) # C:\Users\<tu-usuario>\Barcelona\Sagrada_Familia.txt


# Cambiar archivo destino, manteniendo el resto de la ruta
nuevo_destino = guia.with_name('La_Pedrera.txt')
print(nuevo_destino) # C:\Users\<tu-usuario>\Barcelona\La_Pedrera.txt


# Escalar en los directorios de la ruta
print(guia.parent)        # C:\Users\<tu-usuario>\Barcelona
print(guia.parent.parent) # C:\Users\<tu-usuario>


'''
De aquí en adelante, ejemplos usando el contenido de Europa.rar, el cual
fue entregado y explicado dentro del curso
'''

home = Path(Path.home(), 'Europa')

# Saber qué archivos .txt en carpeta 'Europa' (excl. subdirectorios)
for txt in Path(home).glob('*.txt'):
    print(txt)


# Saber qué archivos .txt en carpeta 'Europa' (incl. subdirectorios)
for txt in Path(home).glob('**/*.txt'):
    print(txt)


guia = Path('Europa', 'España', 'Barcelona', 'Sagrada_Familia.txt')
en_europa = guia.relative_to('Europa')
en_espania = guia.relative_to('Europa', 'España')
print(en_europa)    # España\Barcelona\Sagrada_Familia.txt
print(en_espania)   # Barcelona\Sagrada_Familia.txt

'''
IMPORTANTE
Python devuelve el siguiente warning:

DeprecationWarning: support for 
supplying more than one positional argument to pathlib.PurePath.relative_to() 
is deprecated and scheduled for removal in Python 3.14
    en_espania = guia.relative_to('Europa', 'España')
'''
