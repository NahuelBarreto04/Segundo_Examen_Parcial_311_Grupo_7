import pygame
from funciones.menu import get_dificultad_actual, set_pantalla_actual
from funciones.utilidad import dibujar_boton_volver
from funciones.funciones import *

def pantalla_juego(pantalla, evento):
    dificultad_juego = {}

    pantalla.fill((0,0,0))

    dificultad = get_dificultad_actual()

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
    inicializar_react_celdas(tablero, CELDA, pantalla)

    # Imagen de prueba (borrar después)
    ruta_imagenes = 'imagenes/'
    imagen_celda = pygame.image.load(f"{ruta_imagenes}bloque-vacio.png")
    imagen_celda = pygame.transform.scale(imagen_celda, (120, 220))
    pantalla.blit(imagen_celda, (120, 220))

    # Dibujar boton volver al menu
    if dibujar_boton_volver(pantalla, evento):
        set_pantalla_actual("menu")

    pygame.display.flip()
