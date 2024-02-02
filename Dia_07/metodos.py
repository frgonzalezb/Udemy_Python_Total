class Pajaro:
    '''
    Define cualquier pájaro según especie y color.
    '''
    alas = True

    def __init__(self, especie, color):
        self.especie = especie
        self.color = color

    def piar(self):
        print('Pío')

    def volar(self, metros):
        print(f'El pájaro ha volado {metros} metros.')

    def hablar(self):
        print(f'Mi color es {self.color}')


piolin = Pajaro('Canario', 'amarillo')
print(f'Mi pájaro es un {piolin.especie} y es de color {piolin.color}.')

piolin.piar()
piolin.volar(50)
piolin.hablar()
