def validar_edad(valor):
    if not valor.isnumeric():
        print(f'Valor "{valor}" para "edad" no está permitido.')
        exit()

    return int(valor)


def validar_tienes_licencia(valor):
    if valor == 's':
        valor = True
    elif valor == 'n':
        valor = False
    else:
        print(f'Valor "{valor}" para "tienes_licencia" no está permitido.')
        exit()

    return valor


def imprimir_respuesta(edad, tienes_licencia):
    if edad < 18 and tienes_licencia:
        print('Estás mintiendo, o tu licencia es ilegítima.')
    elif edad < 18 and not tienes_licencia:
        print('Debes ser mayor de 18 años y tener licencia para conducir.')
    elif edad >= 18 and not tienes_licencia:
        print('Debes tener licencia para conducir.')
    else:
        print('Puedes conducir.')


def ejecutar_script():
    try:
        edad = input('Ingresa tu edad: ')
        tienes_licencia = input('¿Tienes licencia de conducir? s/n: ').lower()

        edad = validar_edad(edad)
        tienes_licencia = validar_tienes_licencia(tienes_licencia)

        imprimir_respuesta(edad, tienes_licencia)
        
    except Exception as e:
        print(f'Ha ocurrido un error inesperado: {e}')


ejecutar_script()
