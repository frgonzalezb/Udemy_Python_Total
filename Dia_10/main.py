import pygame
import random
import math

from pygame import mixer


# Inicializar PyGame
pygame.init()


# Crear la ventana
ventana = pygame.display.set_mode((800, 600))


# Fondo, ícono y título de la ventana
fondo = pygame.image.load('./Dia_10/assets/fondo.jpg')
icono = pygame.image.load('./Dia_10/assets/icon.png')
pygame.display.set_icon(icono)
pygame.display.set_caption('Invasión Espacial')


# Añadir música de fondo
mixer.music.load('./Dia_10/assets/musica_fondo.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)


# Contador de puntos
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10


# Variables del jugador
cohete_img = pygame.image.load('./Dia_10/assets/cohete.png')
cohete_x = 800 * 0.5 - 32   # Centrar = 1/2 ancho ventana - 1/2 ancho obj
cohete_y = 600 - 32 - 64    # Bajar = Alto ventana - margen - alto obj
cohete_x_cambio = 0
cohete_y_cambio = 0


# Variables del enemigo
# ovni_img = pygame.image.load('./Dia_10/assets/ovni.png')
ovni_img = []
# ovni_x = random.randint(0, 800 - 64)
ovni_x = []
# ovni_y = random.randint(50, 300 - 64)
ovni_y = []
# ovni_x_cambio = 0.5
ovni_x_cambio = []
# ovni_y_cambio = 32
ovni_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    ovni_img.append(pygame.image.load('./Dia_10/assets/ovni.png'))
    ovni_x.append(random.randint(0, 800 - 64))
    ovni_y.append(random.randint(50, 300 - 64))
    ovni_x_cambio.append(0.5)
    ovni_y_cambio.append(32)


# Variables de la bala
balas = []
bala_img = pygame.image.load('./Dia_10/assets/bala.png')
bala_x = 0
bala_y = 600 - 32 - 64  # A la altura del cohete
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False


# Texto Game Over (d'oh!)
def texto_final():
    game_over = fuente.render('GAME OVER', True, (255, 255, 255))
    ventana.blit(game_over, (60, 200))


# Función principal del puntaje
def mostrar_puntaje(pos_x, pos_y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    ventana.blit(texto, (pos_x, pos_y))


# Función principal del jugador
def jugador(pos_x, pos_y):
    ventana.blit(cohete_img, (pos_x, pos_y))


# Función principal del enemigo
def enemigo(pos_x, pos_y, enemigo):
    ventana.blit(ovni_img[enemigo], (pos_x, pos_y))


# Función principal de la bala
def disparar_bala(pos_x, pos_y):
    global bala_visible # Para que la función modifique bala_visible
    bala_visible = True
    ventana.blit(bala_img, (pos_x + 16, pos_y + 10)) # Sale del cohete


'''
MÉTETE ESTO EN LA CABEZA:

Para hacer un cálculo de colisiones, hay que establecer una distancia 
mínima entre dos objetos en un plano bidimensional, en la cual si es 
menor a X número, hay colisión. Una fórmula muy común en el desarrollo 
de videojuegos (según el profe) para calcular esa distancia es:

D = math.sqrt(pow(x2 - x1) + pow(y2 - y1))

Donde:
-   D es la distancia,
-   x1 e y1 son coordenadas del objeto 1
-   x2 e y2 son coordenadas del objeto 2
'''


def detectar_colision(pos_x1, pos_y1, pos_x2, pos_y2):
    distancia = math.sqrt(
        pow(pos_x2 - pos_x1, 2) + pow(pos_y2 - pos_y1, 2)
    )
    if distancia < 32:
        return True
    return False


'''
MÉTETE ESTO EN LA CABEZA:

Evitar hacer loops infinitos para mantener la ventana abierta, 
ya que la única opción para cerrar será Ctrl + Alt + Supr!!!!!

Un loop adecuado para mantener la ventana abierta sería:

    se_ejecuta = True
    while se_ejecuta:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                se_ejecuta = False
'''


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    
    # Color de fondo RGB
    # ventana.fill((205, 144, 228))

    # Imagen de fondo
    ventana.blit(fondo, (0, 0))

    # Iterar eventos
    for evento in pygame.event.get():
        
        # Cerrar la ventana
        if evento.type == pygame.QUIT:
            # print('adios')
            se_ejecuta = False

        # Si una tecla ha sido presionada
        if evento.type == pygame.KEYDOWN:
            # print('una tecla fue presionada') # dbg
            if evento.key == pygame.K_LEFT:
                # print('flecha izquierda presionada') # dbg
                cohete_x_cambio = -0.5
            if evento.key == pygame.K_RIGHT:
                # print('flecha derecha presionada') # dbg
                cohete_x_cambio = 0.5
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('./Dia_10/assets/disparo.mp3')
                sonido_bala.play()
                nueva_bala = {
                    'x': cohete_x,
                    'y': cohete_y,
                    'velocidad': -5
                }
            balas.append(nueva_bala)
                # if not bala_visible:
                #     bala_x = cohete_x
                #     disparar_bala(bala_x, bala_y)

        # Si una tecla presionada ha sido liberada
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                # print('la tecla fue liberada')
                cohete_x_cambio = 0

    # Modificar ubicación del jugador
    cohete_x += cohete_x_cambio

    # Mantener jugador dentro de la ventana
    if cohete_x <= 0:
        cohete_x = 0
    if cohete_x >= 800 - 64:
        cohete_x = 800 - 64 # Ancho de la ventana - ancho del sprite

    # Modificar ubicación del enemigo
    for e in range(cantidad_enemigos):
        
        # Fin del juego
        if ovni_y[e] >= 450:
            for k in range(cantidad_enemigos):
                ovni_y[k] = 1000    # Ilusión de desaparición
            texto_final()
            break
        
        # Mover enemigos
        ovni_x[e] += ovni_x_cambio[e]

        # Movimiento del enemigo dentro de la ventana
        if ovni_x[e] <= 0:
            ovni_x_cambio[e] = 0.5
            ovni_y[e] += ovni_y_cambio[e]
        if ovni_x[e] >= 800 - 64:
            ovni_x_cambio[e] = -0.5
            ovni_y[e] += ovni_y_cambio[e]

        # Si da en el blanco
        for bala in balas:
            colision = detectar_colision(
                ovni_x[e], ovni_y[e], bala['x'], bala['y']
            )
            if colision:
                sonido_colision = mixer.Sound('./Dia_10/assets/golpe.mp3')
                sonido_colision.play()
                balas.remove(bala)
                # bala_y = 600 - 32 - 64  # A la altura del cohete
                # bala_visible = False
                puntaje += 1
                # print(puntaje) # dbg
                ovni_x[e] = random.randint(0, 800 - 64)
                ovni_y[e] = random.randint(50, 300 - 64)
                break
        
        enemigo(ovni_x[e], ovni_y[e], e)

    # Movimiento bala
    for bala in balas:
        bala['y'] += bala['velocidad']
        ventana.blit(bala_img, (bala['x'] + 16, bala['y'] + 10))
        if bala['y'] < 0:
            balas.remove(bala)
        # if bala_y <= -64:
        #     # Si la bala ha desaparecido completamente de la ventana
        #     bala_y = 600 - 32 - 64  # A la altura del cohete
        #     bala_visible = False
        # if bala_visible:
        #     disparar_bala(bala_x, bala_y)
        #     bala_y -= bala_y_cambio

    
    jugador(cohete_x, cohete_y)
    mostrar_puntaje(texto_x, texto_y)
    
    
    # Actualizar estado de la ventana
    pygame.display.update()


'''
NOTAS ADICIONALES:
-   Créditos a Flaticon y Freekpik por las imágenes.
-   El código viola muchas convenciones en honor a la comprensión del
    funcionamiento básico de PyGame. Queda pendiente refactorizar (por
    ejemplo, usando clases para los objetos y organizando el código en
    distintos módulos y funciones).
'''
