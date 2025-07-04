import pygame
import pygame
from .utilidad import IMAGENES, dibujar_boton_volver, SONIDOS
from .configuraciones import *


def pantalla_puntajes(pantalla, evento):
    # pantalla.fill((0, 0, 0))
    fondo = pygame.transform.scale(IMAGENES["fondo_puntajes"], pantalla.get_size())
    pantalla.blit(fondo, (0, 0))

    fuente_titulo = pygame.font.SysFont("arial", 50)
    texto_titulo = fuente_titulo.render("Puntajes Altos", True, (255, 255, 255))
    rect_titulo = texto_titulo.get_rect(center=(pantalla.get_width() // 2, 100))
    pantalla.blit(texto_titulo, rect_titulo)


    if dibujar_boton_volver(pantalla, evento): 
        set_pantalla_actual("menu")
    pygame.display.flip()




def dibujar_victoria(pantalla):
    fuente = pygame.font.SysFont("arial", 60, bold=True)
    texto = fuente.render("GANASTE!", True, (0, 255, 0))
    sombra = fuente.render("GANASTE!", True, (0, 0, 0))

    x = (pantalla.get_width() - texto.get_width()) // 2
    y = pantalla.get_height() // 2 - texto.get_height() // 2

    fondo_rect = pygame.Rect(x - 20, y - 20, texto.get_width() + 40, texto.get_height() + 40)
    pygame.draw.rect(pantalla, (20, 20, 20), fondo_rect, border_radius=15)

    pantalla.blit(sombra, (x + 3, y + 3))
    pantalla.blit(texto, (x, y))
