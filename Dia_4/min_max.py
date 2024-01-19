menor = min(58, 96, 72, 64, 35)
mayor = max(58, 96, 72, 64, 35)
print(menor)
print(mayor)

lista = [58, 96, 72, 64, 35]
print(f'El menor es {min(lista)} y el mayor es {max(lista)}')

nombres = ['Juan', 'Pablo', 'Alicia', 'María']
print(f'En orden alfabético, el primer nombre es {min(nombres)}')
print(f'En orden alfabético, el último nombre es {max(nombres)}')

nombre = 'Carlos'
print(min(nombre)) # Primero recorre mayúsculas, luego minúsculas
print(min(nombre.lower())) # Aquí sí imprime 'a'

dic = {'C1': 45, 'C2': 11}
print(min(dic)) # Devuelve la primera clave alfanuméricamente: 'C1'
print(min(dic.values())) # Devuelve el valor más pequeño: '11'
