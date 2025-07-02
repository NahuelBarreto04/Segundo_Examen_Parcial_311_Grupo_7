import pygame
#from funciones.menu import mostrar_textos, dibujar_botones, manejar_click, get_pantalla_actual, set_pantalla_actual, dificultad_actual,pantalla_actual
from funciones.pantallas import pantalla_juego
from funciones.menu import *
from funciones.funciones import *
pygame.init()
pygame.font.init()

ANCHO = 800
ALTO = 600

inicio_timer = None
ancho_actual = ANCHO
alto_actual = ALTO
PANTALLA = pygame.display.set_mode((ANCHO, ALTO),)

pygame.display.set_caption("Buscaminas")

COLOR_FONDO = (54, 54, 54)
def actualizar_resolucion():

    ancho, alto = get_resolucion_actual()
    PANTALLA = pygame.display.set_mode((ancho, alto),)

def pantalla_menu():
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
                    set_pantalla_actual("menu")
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if get_pantalla_actual() == "menu":
                    manejar_click(evento.pos)
                    actualizar_resolucion()
            if get_pantalla_actual() == "menu":
                pantalla_menu()
            elif get_pantalla_actual() == "juego":
                
                inicio_timer = pantalla_juego(PANTALLA,evento,inicio_timer)
        

actualizar_resolucion()
menu_interaccion()