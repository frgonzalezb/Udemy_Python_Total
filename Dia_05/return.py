def multiplicar(n1, n2):
    return round(n1 * n2, 2)


def ejecutar_script():
    # Porque... ¿por qué no? 😁
    n1 = float(input('Ingresa un número: '))
    n2 = float(input('Ingresa otro número: '))

    res = multiplicar(n1, n2)
    print(f'{n1} * {n2} = {res}')

ejecutar_script()
