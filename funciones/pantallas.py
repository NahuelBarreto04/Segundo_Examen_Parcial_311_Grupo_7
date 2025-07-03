import pygame
import time
from .utilidad import dibujar_boton_volver, dibujar_tablero, inicializar_react_celdas, MARGEN, TAM_CELDA, IMAGENES
from .funciones import *
from . import configuraciones
inicio_timer = None

def pantalla_juego(pantalla, evento,inicio_timer):

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
        configuraciones.dificultad_juego["filas"] = 8
        configuraciones.dificultad_juego["columnas"] = 8
        configuraciones.dificultad_juego["minas"] = 10
    elif dificultad == "normal":
        desc = "tablero 16x16 con 50 minas"
        configuraciones.dificultad_juego["filas"] = 16
        configuraciones.dificultad_juego["columnas"] = 16
        configuraciones.dificultad_juego["minas"] = 50
    else:
        desc = "tablero 24x24 con 120 minas"
        configuraciones.dificultad_juego["filas"] = 24
        configuraciones.dificultad_juego["columnas"] = 24
        configuraciones.dificultad_juego["minas"] = 120

    texto2 = fuente2.render(desc, True, (200,200,200))
    x2 = 20
    y2 = y + texto.get_height() + 10
    pantalla.blit(texto2, (x2, y2))



    # Generacion de tablero 
    FILAS = configuraciones.dificultad_juego["filas"]
    COLUMNAS = configuraciones.dificultad_juego["columnas"]

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

def dibujar_timer(pantalla,incio):
    fuente = pygame.font.SysFont("arial",30)
    ahora = pygame.time.get_ticks()
    segundos= (ahora - incio) // 1000
    texto = fuente.render("tiempo: " + str(segundos) + "s",True,(255,255,255))
    x = pantalla.get_width() - texto.get_width() - 20
    y =20
    pantalla.blit(texto,(x,y))