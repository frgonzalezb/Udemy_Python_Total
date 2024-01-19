'''
a.k.a. "keyword args"
'''

def ejemplo_kwargs_1(**kwargs):
    print(type(kwargs)) # <class 'dict'>
    print(kwargs) # {'x': 3, 'y': 5, 'z': 2}


def ejemplo_kwargs_2(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')


def ejemplo_kwargs_3(num1, num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')


ejemplo_kwargs_1(x=3, y=5, z=2)
ejemplo_kwargs_2(x=3, y=5, z=2)
ejemplo_kwargs_3(5, 50, 100, 200, 300, 400, x='uno', y='dos', z='tres')

args = [150, 250, 350, 450]
kwargs = {'x': 'cuatro', 'y': 'cinco', 'z': 'seis'}

ejemplo_kwargs_3(1, 10, *args, **kwargs)
