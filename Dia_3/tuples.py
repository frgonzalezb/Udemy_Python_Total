mi_tupla = (1, 2, 3, 4)
print(type(mi_tupla))
print(type(list(mi_tupla)))

# Desempacar valores de tupla a distintas variables
t = (1, 2, 3)
x, y, z = t     # Misma cantidad de variable que elementos en la tupla
print(x, y, z)  # x=1, y=2, z=3

nt = (1, 2, 3, 1, 1, 'canon', 'canon')
print(nt.count(1))          # Cuenta todos los '1' que haya
print(nt.count('canon'))    # Cuenta todos los 'canon' que haya
print(nt.index('canon'))    # Devuelve el índice del primer elemento 'canon'
