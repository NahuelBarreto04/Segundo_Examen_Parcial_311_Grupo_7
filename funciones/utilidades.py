import pygame
from funciones.pantallas import *
from funciones.funciones import *
#BOTON DE INICIO
pygame.init()
boton_ancho = 200
boton_alto = 70
boton_x = (ANCHO / 2 )- (boton_ancho / 2) 
boton_y = (ALTO / 2 ) - (boton_alto / 2)
boton_rect = pygame.Rect(boton_x, boton_y, boton_ancho, boton_alto)
texto_inicio = pygame.font.get_fonts()
boton_texto = "JUGAR"
fuente_boton = pygame.font.Font(None, 50)
texto_color_boton = BLANCO

