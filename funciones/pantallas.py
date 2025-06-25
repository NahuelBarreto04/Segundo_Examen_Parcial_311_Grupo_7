import pygame
from funciones.menu import get_dificultad_actual

def pantalla_juego(pantalla):
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
    elif dificultad == "normal":
        desc = "tablero 16x16 con 50 minas"
    else:
        desc = "tablero 24x24 con 120 minas"
    
    texto2 = fuente2.render(desc,True,(200,200,200))
    x2 = 20
    y2 = y + texto.get_height() +10
    pantalla.blit(texto2,(x2,y2))

    fuente3 = pygame.font.SysFont("arial", 25)
    texto3 = fuente3.render("ESC para volver al menu",True,(180,180,180))
    x3 = 20
    y3 = pantalla.get_height() - texto3.get_height() - 10
    pantalla.blit(texto3,(x3,y3))
    pygame.display.flip()