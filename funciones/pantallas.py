import pygame

ANCHO, ALTO = 800 , 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Buscaminas N")

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)


  

def pantalla_inicio():
    PANTALLA.fill(ROJO)

def pantalla_juego():
    PANTALLA.fill(BLANCO)

