import pygame
# import time
from .utilidad import *
from .funciones import *
from . import configuraciones
inicio_timer = None
MAX_AREA = 600
MAX_ANCHO_TABLERO = 500
MAX_ALTO_TABLERO = 500

def iniciar_juego(pantalla, estado_juego):
    #Estado del Juego
    estado_juego["gano"] = False
    estado_juego["juego_iniciado"] = True
    estado_juego["inicio_timer"] = pygame.time.get_ticks()

    #DIFICULTAD
    dificultad = configuraciones.get_dificultad_actual()
    if dificultad == "facil":
        filas, columnas, minas = 8, 8, 10
    elif dificultad == "normal":
        filas, columnas, minas = 16, 16, 50
    else:
        filas, columnas, minas = 24, 24, 120

    #TAMAÑO DE LAS CELDAS y TABLERO
    ancho_disp = pantalla.get_width() - 100
    alto_disp = pantalla.get_height() - 200

    tam_celda_x = (ancho_disp - MARGEN) // columnas - MARGEN
    tam_celda_y = (alto_disp - MARGEN) // filas - MARGEN
    tam_celda = min(tam_celda_x, tam_celda_y)

    ancho_tablero = columnas * (tam_celda + MARGEN) + MARGEN
    alto_tablero = filas * (tam_celda + MARGEN) + MARGEN

    offset_x = (pantalla.get_width() - ancho_tablero) // 2
    offset_y = (pantalla.get_height() - alto_tablero) // 2


    #GENERAR TABLERO 
    tablero = generar_tablero(filas, columnas, CELDA)
    for fila in range(filas):
        for columna in range(columnas):
            x = offset_x + MARGEN + columna * (tam_celda + MARGEN)
            y = offset_y + MARGEN + fila * (tam_celda + MARGEN)
            tablero[fila][columna]["rect"] = pygame.Rect(x, y, tam_celda, tam_celda)

    estado_juego["tablero"] = tablero
    estado_juego["filas"] = filas
    estado_juego["columnas"] = columnas
    estado_juego["minas"] = minas
    estado_juego["tam_celda"] = tam_celda
    estado_juego["banderas_puestas"] = 0

def dibujar_juego(pantalla, evento, estado_juego):
    pantalla.fill((0, 0, 0))
    fuente = pygame.font.SysFont("arial", 20)
    texto = fuente.render("Dificultad: " + configuraciones.get_dificultad_actual().upper(), True, (255, 255, 255))
    pantalla.blit(texto, (20, 20))

    fuente2 = pygame.font.SysFont("arial", 20)
    if estado_juego["filas"] == 8:
        desc = "tablero 8x8 con 10 minas"
    elif estado_juego["filas"] == 16:
        desc = "tablero 16x16 con 50 minas"
    else:
        desc = "tablero 24x24 con 120 minas"
    texto2 = fuente2.render(desc, True, (200, 200, 200))
    pantalla.blit(texto2, (20, 50))

    dibujar_timer(pantalla, estado_juego)
    dibujar_contador_banderas(pantalla, estado_juego)
    dibujar_tablero(pantalla, estado_juego["tablero"], IMAGENES, estado_juego["perdio"])

    rect_boton_reinicio = dibujar_boton_reinicio(configuraciones.get_pantalla_pygame(), IMAGENES)
    controlar_boton_reinicio(evento, rect_boton_reinicio, estado_juego)
    
    #Victoria

    if estado_juego.get("gano"):
        fuente = pygame.font.SysFont("arial", 60, bold=True)
        texto = fuente.render("GANASTE!", True, (0, 255, 0))
        sombra = fuente.render("GANASTE!", True, (0, 0, 0))

        x = (pantalla.get_width() - texto.get_width()) // 2
        y = pantalla.get_height() // 2 - texto.get_height() // 2

        fondo_rect = pygame.Rect(x - 20, y - 20, texto.get_width() + 40, texto.get_height() + 40)
        pygame.draw.rect(pantalla, (20, 20, 20), fondo_rect, border_radius=15)

        pantalla.blit(sombra, (x + 3, y + 3))
        pantalla.blit(texto, (x, y))

    if estado_juego.get("perdio"):
        fuente = pygame.font.SysFont("arial", 60, bold=True)
        texto = fuente.render("DERROTA", True, (255, 0, 0))
        sombra = fuente.render("DERROTA", True, (0, 0, 0))

        x = (pantalla.get_width() - texto.get_width()) // 2
        y = pantalla.get_height() // 2 - texto.get_height() // 2

        fondo_rect = pygame.Rect(x - 20, y - 20, texto.get_width() + 40, texto.get_height() + 40)
        pygame.draw.rect(pantalla, (20, 20, 20), fondo_rect, border_radius=15)

        pantalla.blit(sombra, (x + 3, y + 3))
        pantalla.blit(texto, (x, y))

    if dibujar_boton_volver(pantalla, evento):
        configuraciones.set_pantalla_actual("menu")
        estado_juego["juego_iniciado"] = False


    pygame.display.flip()








def dibujar_timer(pantalla, estado_juego):
    fuente = pygame.font.SysFont("arial", 30)

    if estado_juego.get("perdio") or estado_juego.get("gano"):
        segundos = estado_juego.get("tiempo_final", 0)
    else:
        ahora = pygame.time.get_ticks()
        segundos = (ahora - estado_juego["inicio_timer"]) // 1000

    texto = fuente.render("tiempo: " + str(segundos) + "s", True, (255, 255, 255))
    x = pantalla.get_width() - texto.get_width() - 20
    y = 20
    pantalla.blit(texto, (x, y))


def dibujar_contador_banderas(pantalla, estado_juego):
    fuente = pygame.font.SysFont("arial", 30)
    banderas = estado_juego.get("banderas_puestas", 0)
    max_banderas = estado_juego.get("minas", 0)
    texto = fuente.render("Banderas: " + str(banderas) + " / " + str(max_banderas), True, (255, 255, 255))
    x = 20
    y = 80
    pantalla.blit(texto, (x, y))



#BOTON REINICIO
def dibujar_boton_reinicio(pantalla, imagenes):
    ancho_boton = 60
    alto_boton = 60
    x = pantalla.get_width() // 2 - ancho_boton // 2
    y = 20
    rect_reinicio = pygame.Rect(x, y, ancho_boton, alto_boton)
    
    imagen_escalada = pygame.transform.scale(imagenes["cara"], (ancho_boton, alto_boton))
    
    pantalla.blit(imagen_escalada, rect_reinicio)

    return rect_reinicio


def controlar_boton_reinicio(evento, rect_reinicio, estado_juego):
    if evento is not None and evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        if rect_reinicio.collidepoint(evento.pos):
            resetear_juego(estado_juego)
            return True
    return False









