import pyttsx3
import speech_recognition as sr # Requiere setuptools!!
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import datetime
import wikipedia


# Escuchar nuestro micrófono y devolver el audio como texto
def transformar_audio_en_texto():
    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar micrófono
    with sr.Microphone() as origen:
        # Tiempo de espera
        r.pause_threshold = 0.5 # Si AssertionError, ajustar esto

        # Informar que comenzó la grabación
        print('Ya puedes hablar.')

        # Guardar lo que escuche como audio
        audio = r.listen(origen)


        try:
            # Buscar en google lo escuchado
            pedido = r.recognize_google(audio, language='es-cl')

            # Prueba de que pudo ingresar
            print('Dijiste: ' + pedido)

            # Devolver pedido
            return pedido
        
        # En caso de que no comprenda el audio
        except sr.UnknownValueError:
            # Prueba de que no comprendió el audio
            print('Ups, no entendí.')

            # Devolver error
            return 'Sigo esperando...'
        
        # En caso de no resolver el pedido
        except sr.RequestError:
            # Prueba de que no comprendió el audio
            print('Hubo un problema en resolver el pedido.')

            # Devolver error
            return 'Sigo esperando...'
        
        # Error inesperado
        except:
            # Prueba de que no comprendió el audio
            print('Ha ocurrido un error inesperado.')

            # Devolver error
            return 'Sigo esperando...'




def hablar(mensaje):
    '''Función para que el asistente pueda ser escuchado'''

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()

    # Ajustar la velocidad de la voz
    engine.setProperty('rate', 125)

    # Ver las voces disponibles
    # for voice in engine.getProperty('voices'):
    #     print(voice)

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


def pedir_dia():
    '''Informar el día de la semana'''

    # Crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # Crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario con nombres de días
    calendario = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo',
    }

    # Decir el día de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


def pedir_hora():
    '''Informar que hora es.'''
    hora = datetime.datetime.now()
    hora = f'Son las {hora.hour} horas con {hora.minute} minutos.'
    print(hora)
    hablar(hora)


def saludar():
    '''(Autoexplicatorio)'''
    hora = datetime.datetime.now()
    print(hora)
    if hora.hour > 6 and hora.hour <= 12:
        momento = 'Buenos días'
    elif hora.hour > 12 and hora.hour <= 20:
        momento = 'Buenas tardes'
    else:
        momento = 'Buenas noches'
        
    presentacion = f'{momento}, soy tu asistente personal. '
    disposicion = 'Por favor, dime en qué puedo ayudar. '
    hablar(presentacion + disposicion)


def pedir_cosas():
    '''Función principal del asistente virtual.'''
    saludar()     
    comenzar = True
    while comenzar:
        # Activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir navegador' in pedido:
            hablar('Abriendo tu navegador predeterminado...')
            webbrowser.open('https://www.google.com/')
            continue
        elif 'abrir youtube' in pedido:
            hablar('Abriendo YouTube...')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'salir' in pedido:
            hablar('Hasta pronto.')
            break
        else:
            hablar('No entiendo lo que dices.')
        

# Usage
# transformar_audio_en_texto()
# hablar('Hola, mundo')
# pedir_dia()
# pedir_hora()
# saludar()
pedir_cosas()
