def obtener_cafe_mas_caro(lista_precios):
    cafe_mas_caro = ''
    precio_mayor = 0

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe

    return (cafe_mas_caro, precio_mayor)


precios_cafe = [
    ('Capuccino', 1.5),
    ('Expresso', 1.2),
    ('Moka', 1.8),
]

cafe, precio = obtener_cafe_mas_caro(precios_cafe)
print(f'El café más caro es {cafe}, cuyo precio es USD {precio}')
