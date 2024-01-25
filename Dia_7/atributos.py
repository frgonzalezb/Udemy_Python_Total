class Ejemplo:
    '''
    Ejemplo para clarificar atributos de:
    - clase: cada objeto de la misma clase tiene los mismos atributos
    - instancia: cada objeto de la misma clase puede tener valores distintos

    Si se declaran atributos de instancia, se deben pasar los valores
    como parámetros al momento de crear un objeto.

    NOTA MENTAL: self es obligatorio y representa a la instancia
    (objeto) de la clase
    '''
    atributo_clase = 'Valor general'

    # Método constructor
    def __init__(self, parametro):
        self.atributo_instancia = parametro


mi_ejemplo_1 = Ejemplo('Valor particular 1')
mi_ejemplo_2 = Ejemplo('Valor particular 2')
print(mi_ejemplo_1.atributo_clase)      # Valor general
print(mi_ejemplo_1.atributo_instancia)  # Valor particular 1
print(mi_ejemplo_2.atributo_clase)      # Valor general
print(mi_ejemplo_2.atributo_instancia)  # Valor particular 2


class Pajaro:
    '''
    Define cualquier pájaro según especie y color.
    '''
    alas = True

    def __init__(self, especie, color):
        self.especie = especie
        self.color = color


mi_pajaro = Pajaro('Tucán', 'negro')
print(f'Mi pájaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}.')
