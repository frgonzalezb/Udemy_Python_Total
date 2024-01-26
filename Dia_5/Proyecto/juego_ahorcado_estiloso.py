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
from colored import Fore, Style


# Colores
RED = Fore.red
YELLOW = Fore.yellow
GREEN = Fore.green
CYAN = Fore.cyan
BLUE = Fore.blue
MAGENTA = Fore.magenta
RESET = Style.reset


def escoger_dificultad():
    print('1: Cheems')
    print('2: Wojak')
    print('3: Doge')
    print('4: Gigachad')
    msg = f'{MAGENTA}Escoje el nivel de dificultad (1 | 2 | 3 | 4):{RESET} '
    return input(msg)


def obtener_palabra_secreta():
    while True:
        nivel = escoger_dificultad()

        if nivel == '1':
            # Palabras de 4 letras, excl. ñ, x, z
            palabras = [
                'agua',
                'bala',
                'casa',
                'dado',
                'edad',
                'frio',
                'gato',
                'hilo',
                'isla',
                'jara',
                'kilo',
                'lana',
                'mano',
                'nada',
                'ojos',
                'pera',
                'rata',
                'sala',
                'todo',
                'uvas',
                'velo',
                'yate',
            ]
            break
        elif nivel == '2':
            # Palabras de 5 a 10 letras, incl. ñ, x, z
            palabras = [
                'amistad',
                'balance',
                'cuadrado',
                'delantal',
                'elefante',
                'familia',
                'guitarra',
                'humanidad',
                'ingenio',
                'jaqueca',
                'keroseno',
                'libertad',
                'maligno',
                'naturaleza',
                'ñandues',
                'ordeñar',
                'perros',
                'quesillo',
                'roedores',
                'salinidad',
                'temporal',
                'ubicacion',
                'violeta',
                'webinar',
                'xilofono',
                'yugular',
                'zorrillo'
            ]
            break
        elif nivel == '3':
            # Palabras de más de diez letras, algo rebuscadas
            palabras = [
                'autodeterminacion',
                'bienaventurados',
                'contrarrevolucionario',
                'desoxirribonucleotidos',
                'electroencefalografista',
                'fundacionales',
                'globalitarismo',
                'hermafroditismo',
                'incomprehensibilidad',
                'jeffersonianos',
                'kinesiologia',
                'lenguilargo',
                'mancomunidad',
                'neoliberalismo',
                'otorrinolaringologo',
                'psicoestimulante',
                'quilopleura',
                'rinofaringitis',
                'supranacionalidad',
                'territorialidad',
                'universalismo',
                'vulcaniforme',
                'xenofobicos',
                'yacimiento',
                'zanquituerto',
            ]
            break
        if nivel == '4':
            # Selección de palabras God-level
            palabras = [
                'arbeiterunfallverischerungsgesetz',
                'bundesprasidentenstichwahlwiederholungsverschiebung',
                'chargoggagoggmanchauggagoggchaubunagungamaugg',
                'diethylaminopropionylethoxycarbonylaminophenothiazine',
                'hippopotomonstrosesquipedaliophobia',
                'llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch',
                'miinibaashkiminasiganibiitoosijiganibadagwiingweshiganibakwezhigan',
                'rindfleischetikettierungsuberwachungsaufgabenubertragungsgesetz',
                'taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu',
            ]
            break
        else:
            print(f'{RED}Opción no válida.{RESET}')
    
    return choice(palabras)


def ocultar_palabra_secreta(palabra):
    lista = []
    for letra in palabra:
        lista.append('_')
    return lista


def pedir_letra():
    return input('\nDame una letra: ').lower()


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


def mostrar_desafio(jugador, intentos, palabra_oculta):
    saludos = f'\n{BLUE}¡Hola, {jugador}!{RESET}'
    consigna = f'\n{CYAN}Adivina la palabra para ganar:{RESET}\n'
    desafio = f'\n{' '.join(palabra_oculta)}'

    if len(intentos) == 0:
        return print(saludos + consigna + desafio)
    
    return print(consigna + desafio)


def mostrar_intentos(intentos):
    if len(intentos) >= 1:
        print(f'{CYAN}Tus intentos recientes:{RESET} {intentos}')


def mostrar_mensaje_vidas(vidas):
    if vidas == 6:
        print(f'\nTienes {GREEN}{vidas}{RESET} vidas.')
    elif 1 < vidas < 6:
        print(f'\nTe restan {YELLOW}{vidas}{RESET} vidas.')
    else:
        print(f'\n{RED}¡Te queda sólo 1 vida!{RESET} 😱')


def actualizar_pantalla(jugador, palabra_oculta, vidas, intentos):
    mostrar_desafio(jugador, intentos, palabra_oculta)
    mostrar_mensaje_vidas(vidas)
    mostrar_intentos(intentos)  


def mostrar_acierto_o_desacierto(acierto: bool, letra: str):
    if acierto:
        mensaje = f'{GREEN}¡Qué bien!{RESET} '
        detalle = f'La letra "{letra.upper()}" está en la palabra. 👍'
    else:
        mensaje = f'{RED}¡Qué mal!{RESET} '
        detalle = f'La letra "{letra.upper()}" no está en la palabra.'

    return print(mensaje + detalle)


def mostrar_alerta(mensaje):
    '''
    Imprime en consola un mensaje de alerta con letras amarillas.
    '''
    return print(f'{YELLOW}{mensaje}{RESET}')


def mostrar_error(mensaje):
    '''
    Imprime en consola un mensaje de error con letras rojas.
    '''
    return print(f'{RED}{mensaje}{RESET}')


def mostrar_pantalla_final(ganador: bool, jugador, palabra):
    if ganador:
        nombre = f'¡FELICITACIONES, {jugador.upper()}!'
        oculta = f'"{GREEN}{palabra.upper()}{RESET}"'
        titulo = f'\n🥳 {BLUE}{nombre}{RESET} 🥳'
        mensaje = f'\nEncontraste la palabra oculta: {oculta}'

        return print(titulo + mensaje)
    
    else:
        oculta = f'"{YELLOW}{palabra.upper()}{RESET}"'
        titulo = f'\n{RED}¡Te has quedado sin vidas!{RESET} 💀'
        mensaje = f'\nLa palabra oculta era: {oculta}\n'
        game_over = f'\n{RED}*** GAME OVER ***{RESET}'

        return print(titulo + mensaje + game_over)


def ejecutar_juego(jugador, cantidad_vidas=6):
    vidas = cantidad_vidas
    palabra = obtener_palabra_secreta()
    oculta = ocultar_palabra_secreta(palabra)
    intentos = []

    while vidas > 0:
        actualizar_pantalla(jugador, oculta, vidas, intentos)

        letra = pedir_letra()

        if letra in intentos:
            mostrar_alerta(f'Ya has ingresado "{letra.upper()}" previamente.')
            continue
        
        intentos.append(letra)

        if not validar_letra(letra):
            mostrar_error(f'El caracter "{letra}" no es válido.')
            vidas -= 1
            continue

        if not verificar_letra_en_palabra(letra, palabra):
            mostrar_acierto_o_desacierto(False, letra)
            vidas -= 1
            continue

        indices = obtener_indices(letra, palabra)

        for index, elemento in enumerate(oculta):
            if index in indices:
                oculta[index] = letra.upper()

        mostrar_acierto_o_desacierto(True, letra)

        if ''.join(oculta) == palabra.upper():
            mostrar_pantalla_final(True, jugador, palabra)
            break
    else:
        mostrar_pantalla_final(False, jugador, palabra)


ejecutar_juego(input(f'{MAGENTA}Tu nombre:{RESET} '))
