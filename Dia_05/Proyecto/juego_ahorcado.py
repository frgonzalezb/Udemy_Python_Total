'''
JUEGO 'EL AHORCADO'

CONSIGNA:
- El programa deberá escoger una palabra secreta.
- El programa sólo deberá mostrar como guiones las letras de la palabra.
- El jugador comienza con 6 vidas.
- El jugador deberá cada turno ingresar una letra.
- Si la letra está presente en la palabra:
    - El sistema cambia el guion o los guiones por la letra especificada.
- Si la letra no está presente:
    - El jugador pierde una vida.
- Si el jugador pierde todas las vidas: GAME OVER
- El jugador debe descubrir todas las letras de la palabra para ganar.

TIPS:
- Importar choice
- Crear funciones para:
    - Pedir letra
    - Validar letra
    - Chequear letra en palabra
    - Verificar si jugador ganó
    - etc.
'''

from random import choice


def obtener_palabra_secreta():
    palabras = [
        'agua',
        'benefactor',
        'cerebro',
        'delantal',
        'eclipse',
        'familia',
        'guitarra',
        'humano',
        'ingenio',
        'jalea',
        'keroseno',
        'libertad',
        'materializacion',
        'naturaleza',
        'ñandu',
        'onomatopeya',
        'propiedad',
        'quesadilla',
        'radioactividad',
        'sintetizador',
        'testarudo',
        'unificacion',
        'violeta',
        'webinar',
        'xilofono',
        'yugular',
        'zorrillo'
    ]
    return choice(palabras)


def ocultar_palabra_secreta(palabra):
    lista = []
    for letra in palabra:
        lista.append('_')
    return lista


def pedir_letra():
    return input('Dame una letra: ').lower()


def validar_letra(letra):
    return letra.isalpha()


def verificar_letra_en_palabra(letra, palabra):
    return letra in palabra


def obtener_indices(letra, palabra):
    lista = enumerate(palabra)
    indices = []
    for index, elemento in lista:
        if elemento == letra:
            indices.append(index)
    return indices


def mostrar_desafio(palabra_oculta):
    print(f'\nAdivina la palabra:\n{palabra_oculta}')


def mostrar_intentos(intentos):
    if len(intentos) >= 1:
        print(f'Tus intentos recientes: {intentos}')


def mostrar_mensaje_vidas(vidas):
    if vidas == 6:
        print(f'Tienes {vidas} vidas.')
    elif 1 < vidas < 6:
        print(f'Te restan {vidas} vidas.')
    else:
        print(f'¡Te queda sólo 1 oportunidad!')


def actualizar_pantalla(palabra_oculta, vidas, intentos):
    mostrar_desafio(palabra_oculta)
    mostrar_mensaje_vidas(vidas)
    mostrar_intentos(intentos)


def ejecutar_juego(cantidad_vidas=6):
    vidas = cantidad_vidas
    palabra = obtener_palabra_secreta()
    oculta = ocultar_palabra_secreta(palabra)
    intentos = []

    while vidas > 0:
        actualizar_pantalla(oculta, vidas, intentos)

        letra = pedir_letra()

        if letra in intentos:
            print(f'Ya has ingresado "{letra.upper()}" previamente.')
            continue
        
        intentos.append(letra)

        if not validar_letra(letra):
            print(f'El caracter "{letra}" no es válido.')
            vidas -= 1
            continue

        if not verificar_letra_en_palabra(letra, palabra):
            print(f'La letra "{letra.upper()}" no está en la palabra.')
            vidas -= 1
            continue

        indices = obtener_indices(letra, palabra)

        for index, elemento in enumerate(oculta):
            if index in indices:
                oculta[index] = letra.upper()

        if ''.join(oculta) == palabra.upper():
            print('¡FELICITACIONES!')
            print(f'Encontraste la palabra "{palabra.upper()}".')
            break
    else:
        print('Te has quedado sin vidas. Lamentable.')
        print(f'La palabra oculta era "{palabra.upper()}".')
        print('GAME OVER')


ejecutar_juego()
