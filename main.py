import pygame
from funciones.menu import mostrar_textos, dibujar_botones, manejar_click, get_pantalla_actual, set_pantalla_actual
from funciones.pantallas import pantalla_juego

pygame.init()
pygame.font.init()

ANCHO = 1820
ALTO = 920
PANTALLA = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)
pygame.display.set_caption("Buscaminas")

COLOR_FONDO = (54, 54, 54)

def pantalla_menu():
    PANTALLA.fill(COLOR_FONDO)
    mostrar_textos(PANTALLA)
    dibujar_botones(PANTALLA)
    pygame.display.flip()

def menu_interaccion():
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

        if get_pantalla_actual() == "menu":
            pantalla_menu()
        elif get_pantalla_actual() == "juego":
            pantalla_juego(PANTALLA)


menu_interaccion()
