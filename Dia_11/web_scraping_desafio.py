import bs4
import requests


# Explorar múltiples páginas en un sitio (que compartan un patrón)
url_base = 'https://books.toscrape.com/'
url_catalogo = url_base + 'catalogue/page-{}.html'
for n in range(1, 11):
    print(url_catalogo.format(n))


# Identificar condiciones de extracción
resultado = requests.get(url_catalogo.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
libros = sopa.select('.product_pod')


# Extraer el título de un libro
ejemplo = libros[0].select('a')[1]['title']
print(f'El título del libro en el índice 0 es "{ejemplo}"')


# Combinar items buscados
titulos_rating_alto = []

for pagina in range(1, 51):
    # Crear sopa en cada página
    url_pagina = url_catalogo.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # Iterar libros
    for libro in libros:
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            titulo_libro = libro.select('a')[1]['title']
            titulos_rating_alto.append(titulo_libro)


for t in titulos_rating_alto:
    print(t)
