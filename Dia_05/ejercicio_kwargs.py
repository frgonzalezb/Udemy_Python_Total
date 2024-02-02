def cantidad_atributos(**kwargs):
    '''
    Cuenta la cantidad de parámetros que se entregan,
    y devuelve esa cantidad como resultado.
    '''
    return len(kwargs)


def lista_atributos(**kwargs):
    return list(kwargs.values())


def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}:')

    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')


print(cantidad_atributos(x=1, y=2, z=3))
print(lista_atributos(x=1, y=2, z=3))
describir_persona('María', color_ojos='azules', color_pelo='rubio')
