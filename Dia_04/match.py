'''
match está disponible desde Python versión 3.10 en adelante.
Es similar a switch o switch-case que hay en otros lenguajes.
'''
# Sin match
serie = 'N-02'

if serie == 'N-01':
    print('Samsung')
elif serie == 'N-02':
    print('Nokia')
elif serie == 'N-03':
    print('Motorola')
else:
    print('No existe este producto.')

# Con match
match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case 'N-03':
        print('Motorola')
    case _:
        print('No existe este producto.')


# Ejemplo de la potencia de match más allá de lo anterior
# Ya que puede detectar patrones !!!!!!!
cliente = {
    'nombre': 'Federico', 
    'edad': 45, 
    'ocupacion': 'instructor'
}

pelicula = {
    'titulo': 'Matrix',
    'ficha_tecnica': {
        'protagonista': 'Keanu Reeves', 
        'director': 'Lana y Lilly Wachowski'
    }
}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {
            'nombre': nombre,
            'edad': edad,
            'ocupacion': ocupacion
        }:
            print(f'{nombre} tiene {edad} años, trabaja como {ocupacion} y es un cliente de nuestro cine.')
        case {
            'titulo': titulo,
            'ficha_tecnica': {
                'protagonista': protagonista,
                'director': director
            }
        }:
            print(f'La película {titulo} fue dirigida por {director} y es protagonizada por {protagonista}.')
        case _:
            print(f'No se ha encontrado información relevante para el elemento "{e}".')
