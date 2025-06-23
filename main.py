import pygame
import sys
from funciones.funciones import *
from funciones.pantallas import *
from funciones.utilidades import *
pygame.init()

CLOCK = pygame.time.Clock()
FPS = 60 



RUN = True
mostrar_inicio = True
while RUN:
    CLOCK.tick(FPS)
    if mostrar_inicio:
        pantalla_inicio()
        dibujar_boton(PANTALLA,boton_rect,ROJO, boton_texto, fuente_boton, texto_color_boton)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mostrar_inicio = False
    else:
        pantalla_juego()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False