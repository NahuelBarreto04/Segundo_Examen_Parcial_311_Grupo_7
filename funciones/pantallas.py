import pygame
import time
from .utilidad import *
from .funciones import *
from . import configuraciones
inicio_timer = None

def pantalla_juego(pantalla, evento,inicio_timer):
    dificultad_juego = {}

    pantalla.fill((0,0,0))

    if inicio_timer == None:
        inicio_timer = pygame.time.get_ticks()

        
    dificultad = configuraciones.get_dificultad_actual()

    fuente = pygame.font.SysFont("arial",50)
    texto = fuente.render(f"Dificultad: {dificultad.upper()}",True,(255,255,255))
    x = 20
    y = 20
    pantalla.blit(texto,(x,y))

    fuente2 = pygame.font.SysFont("arial", 30)
    if dificultad == "facil":
        desc = "tablero 8x8 con 10 minas"
        dificultad_juego["filas"] = 8
        dificultad_juego["columnas"] = 8
        dificultad_juego["minas"] = 10
    elif dificultad == "normal":
        desc = "tablero 16x16 con 50 minas"
        dificultad_juego["filas"] = 16
        dificultad_juego["columnas"] = 16
        dificultad_juego["minas"] = 50
    else:
        desc = "tablero 24x24 con 120 minas"
        dificultad_juego["filas"] = 24
        dificultad_juego["columnas"] = 24
        dificultad_juego["minas"] = 120

    texto2 = fuente2.render(desc, True, (200,200,200))
    x2 = 20
    y2 = y + texto.get_height() + 10
    pantalla.blit(texto2, (x2, y2))



    # Lógica del tablero
    tablero = generar_tablero(dificultad_juego["filas"], dificultad_juego["columnas"], CELDA)
    generar_minas(tablero, dificultad_juego["minas"], CELDA)

    FILAS = dificultad_juego["filas"]
    COLUMNAS = dificultad_juego["columnas"]

    ANCHO_TABLERO = COLUMNAS * (TAM_CELDA + MARGEN) + MARGEN
    ALTO_TABLERO = FILAS * (TAM_CELDA + MARGEN) + MARGEN
    
    inicializar_react_celdas(tablero, pantalla, MARGEN, TAM_CELDA, ANCHO_TABLERO, ALTO_TABLERO)

    
    dibujar_tablero(pantalla,tablero, IMAGENES)

    dibujar_timer(pantalla, inicio_timer)

    if dibujar_boton_volver(pantalla,evento):
        configuraciones.set_pantalla_actual("menu")
        return None

    # Dibujar boton volver al menu
    if dibujar_boton_volver(pantalla, evento):
        configuraciones.set_pantalla_actual("menu")

    pygame.display.flip()
    return inicio_timer

def dibujar_timer(pantalla, estado_juego):
    fuente = pygame.font.SysFont("arial", 30)
    
    if estado_juego.get("perdio"):
        segundos = estado_juego.get("tiempo_final", 0)
    else:
        ahora = pygame.time.get_ticks()
        segundos = (ahora - estado_juego["inicio_timer"]) // 1000

    texto = fuente.render("tiempo: " + str(segundos) + "s", True, (255, 255, 255))
    x = pantalla.get_width() - texto.get_width() - 20
    y = 20
    pantalla.blit(texto, (x, y))


MAX_AREA = 600

MAX_ANCHO_TABLERO = 500
MAX_ALTO_TABLERO = 500

def iniciar_juego(pantalla, estado_juego):
    estado_juego["juego_iniciado"] = True
    estado_juego["inicio_timer"] = pygame.time.get_ticks()

    dificultad = configuraciones.get_dificultad_actual()
    if dificultad == "facil":
        filas, columnas, minas = 8, 8, 10
    elif dificultad == "normal":
        filas, columnas, minas = 16, 16, 50
    else:
        filas, columnas, minas = 24, 24, 120

    ancho_disp = pantalla.get_width() - 100
    alto_disp = pantalla.get_height() - 200

    tam_celda_x = (ancho_disp - MARGEN) // columnas - MARGEN
    tam_celda_y = (alto_disp - MARGEN) // filas - MARGEN
    tam_celda = min(tam_celda_x, tam_celda_y)

    ancho_tablero = columnas * (tam_celda + MARGEN) + MARGEN
    alto_tablero = filas * (tam_celda + MARGEN) + MARGEN

    offset_x = (pantalla.get_width() - ancho_tablero) // 2
    offset_y = (pantalla.get_height() - alto_tablero) // 2

    tablero = generar_tablero(filas, columnas, CELDA)
    for f in range(filas):
        for c in range(columnas):
            x = offset_x + MARGEN + c * (tam_celda + MARGEN)
            y = offset_y + MARGEN + f * (tam_celda + MARGEN)
            tablero[f][c]["rect"] = pygame.Rect(x, y, tam_celda, tam_celda)

    estado_juego["tablero"] = tablero
    estado_juego["filas"] = filas
    estado_juego["columnas"] = columnas
    estado_juego["minas"] = minas
    estado_juego["tam_celda"] = tam_celda







def dibujar_juego(pantalla, evento, estado_juego):
    pantalla.fill((0, 0, 0))

    fuente = pygame.font.SysFont("arial", 50)
    texto = fuente.render("Dificultad: " + configuraciones.get_dificultad_actual().upper(), True, (255, 255, 255))
    pantalla.blit(texto, (20, 20))

    fuente2 = pygame.font.SysFont("arial", 30)
    if estado_juego["filas"] == 8:
        desc = "tablero 8x8 con 10 minas"
    elif estado_juego["filas"] == 16:
        desc = "tablero 16x16 con 50 minas"
    else:
        desc = "tablero 24x24 con 120 minas"

    texto2 = fuente2.render(desc, True, (200, 200, 200))
    pantalla.blit(texto2, (20, 80))

    dibujar_tablero(pantalla, estado_juego["tablero"], IMAGENES)
    dibujar_timer(pantalla, estado_juego)

    # ✅ EL BOTON SIEMPRE SE DIBUJA
    if dibujar_boton_volver(pantalla, evento):
        configuraciones.set_pantalla_actual("menu")
        estado_juego["juego_iniciado"] = False

    pygame.display.flip()

