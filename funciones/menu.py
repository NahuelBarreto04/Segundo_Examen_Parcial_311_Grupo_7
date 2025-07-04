import pygame
from . import configuraciones
from funciones.utilidad import IMAGENES


BOTONES = []


def mostrar_textos(pantalla):
    fuente = pygame.font.SysFont("arial", pantalla.get_height() // 8)
    texto = fuente.render("BUSCAMINAS", True, (255, 102, 102))

    padding = 20
    ancho = texto.get_width() + padding
    alto = texto.get_height() + padding
    x = (pantalla.get_width() - ancho) // 2
    y = 30

    rect_fondo = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(pantalla, (100, 100, 100), rect_fondo)  # Fondo gris como los botones

    pantalla.blit(texto, (x + padding // 2, y + padding // 2))


def pantalla_menu(pantalla):
    # Escala la imagen de fondo al tamaño pantalla
    imagen_fondo = pygame.transform.scale(IMAGENES["fondo"], (pantalla.get_width(), pantalla.get_height()))
    pantalla.blit(imagen_fondo, (0, 0))

    mostrar_textos(pantalla)
    dibujar_botones(pantalla)


def dibujar_botones(pantalla):
    BOTONES.clear()
    textos = ["Jugar", f"Dificultad: ({configuraciones.get_dificultad_actual()})", "Puntajes", f"resoluciones ({configuraciones.configuracion_juego['resolucion_actual']})", "Salir"]


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
        ver_puntajes(estado_juego)
    elif indice == 3:
        configuraciones.cambiar_resolucion()
    elif indice == 4:
        salir()

def jugar(estado_juego):
    # estado_juego.clear()
    estado_juego["juego_iniciado"] = False
    estado_juego["perdio"] = False
    configuraciones.set_pantalla_actual("juego")




def ver_puntajes(estado_juego):
    print("PUNTAJES")
    configuraciones.set_pantalla_actual("puntaje")

def salir():
    pygame.quit()
    exit()
