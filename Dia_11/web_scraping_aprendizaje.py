import bs4
import requests


# Extraer el título de la página
url = 'https://books.toscrape.com/'
resultado = requests.get(url)
print(type(resultado))      # <class 'requests.models.Response'>
# print(resultado.text)     # Todo el código fuente de la página

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
# print(sopa)                           # Todo el código fuente, pero parseado
print(type(sopa))                       # <class 'bs4.BeautifulSoup'>
print(sopa.select('title'))             # Lista con toda la etiqueta <title>
print(sopa.select('h1'))                # Lista de todos los elementos <h1>
print(sopa.select('meta'))              # Lista de todos los elementos <meta>
print(len(sopa.select('meta')))         # Se pueden usar todos los métodos list
print(sopa.select('h1')[0].getText())   # Contenido puro de la etiqueta <title>


# Extraer elementos de una clase
columna_lateral = sopa.select('.side_categories')

for article in columna_lateral:
    print(article.getText())


# Extraer imágenes
imagenes = sopa.select('.thumbnail')
print(imagenes[0]['src'])

obtener_imgs = requests.get(url + imagenes[0]['src'])

f = open('./Files/mi_imagen_webscraping.jpg', 'wb') # wb = write binary
f.write(obtener_imgs.content)
f.close()
