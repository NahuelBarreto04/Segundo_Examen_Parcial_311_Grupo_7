import pygame
import sys

pygame.init()

ANCHO, ALTO = 800 , 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Buscaminas N")

CLOCK = pygame.time.Clock()
FPS = 60 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

RUN = True

while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False