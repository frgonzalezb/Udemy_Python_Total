from random import randint


def lanzar_dados():
    return (randint(1, 6), randint(1, 6))


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    
    if suma_dados <= 6:
        return f'La suma de tus dados es {suma_dados}. Lamentable.'
    elif 6 < suma_dados < 10:
        return f'La suma de tus dados es {suma_dados}. Tienes buenas chances.'
    else:
        return f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora.'


dado1, dado2 = lanzar_dados()
print(evaluar_jugada(dado1, dado2))
        