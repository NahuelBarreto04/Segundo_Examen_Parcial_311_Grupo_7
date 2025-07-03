import pygame
#from funciones.menu import mostrar_textos, dibujar_botones, manejar_click, get_pantalla_actual, set_pantalla_actual, dificultad_actual,pantalla_actual
from funciones.pantallas import pantalla_juego
from funciones.menu import *
from funciones.funciones import *
from funciones import configuraciones

pygame.init()
pygame.font.init()
pygame.display.set_caption("Buscaminas")

COLOR_FONDO = (54, 54, 54)
ANCHO_INICIAL, ALTO_INICIAL = configuraciones.get_resolucion_actual()
PANTALLA = pygame.display.set_mode((ANCHO_INICIAL, ALTO_INICIAL), pygame.SCALED)
configuraciones.set_pantalla_pygame(PANTALLA)
inicio_timer = None

def pantalla_menu():
    PANTALLA = configuraciones.get_pantalla_pygame()
    PANTALLA.fill(COLOR_FONDO)
    mostrar_textos(PANTALLA)
    dibujar_botones(PANTALLA)
    pygame.display.flip()

def menu_interaccion():
    global inicio_timer
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    configuraciones.set_pantalla_actual("menu")
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if configuraciones.get_pantalla_actual() == "menu":
                    manejar_click(evento.pos)
                    # configuraciones.actualizar_resolucion()
        if configuraciones.get_pantalla_actual() == "menu":
                pantalla_menu()
        elif configuraciones.get_pantalla_actual() == "juego":
                pantalla_juego(configuraciones.get_pantalla_pygame(), evento, inicio_timer)
                # inicio_timer = pantalla_juego(PANTALLA,evento,inicio_timer)
        

# actualizar_resolucion()
menu_interaccion()