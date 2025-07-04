import pygame
from . import configuraciones
from funciones.menu import *


BOTONES = []


def mostrar_textos(pantalla):
    fuente = pygame.font.SysFont("arial", pantalla.get_height() // 8)
    texto = fuente.render("BUSCAMINAS", True, (255, 255, 255))
    x = (pantalla.get_width() - texto.get_width()) // 2
    y = 30
    pantalla.blit(texto, (x, y))


def dibujar_botones(pantalla):
    BOTONES.clear()
    textos = ["Jugar", f"Dificultad: ({configuraciones.get_dificultad_actual()})", "Puntajes",f"resoluciones ({configuraciones.configuracion_juego["resolucion_actual"]})" ,"Salir"]

    for i in range(len(textos)):
        w = pantalla.get_width() // 4
        h = pantalla.get_height() // 12
        x = (pantalla.get_width() - w) // 2
        y = pantalla.get_height() // 3 + i * (h + 20)

        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(pantalla, (100, 100, 100), rect)

        fuente = pygame.font.SysFont("arial", h // 2)
        texto = fuente.render(textos[i], True, (255, 255, 255))
        pantalla.blit(texto, (x + (w - texto.get_width()) // 2, y + (h - texto.get_height()) // 2))

        BOTONES.append(rect) 

def manejar_click(pos, estado_juego):
    for i in range(len(BOTONES)):
        if BOTONES[i].collidepoint(pos):
            ejecutar_funcion(i, estado_juego)

def ejecutar_funcion(indice, estado_juego):
    if indice == 0:
        jugar(estado_juego)
    elif indice == 1:
        configuraciones.cambiar_dificultad()
    elif indice == 2:
        ver_puntajes()
    elif indice == 3:
        configuraciones.cambiar_resolucion()
    elif indice == 4:
        salir()

def jugar(estado_juego):
    # estado_juego.clear()
    estado_juego["juego_iniciado"] = False
    estado_juego["perdio"] = False
    configuraciones.set_pantalla_actual("juego")




def ver_puntajes():
    print("PUNTAJES")

def salir():
    pygame.quit()
    exit()
