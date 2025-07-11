import pygame
from . import configuraciones
from funciones.utilidad import IMAGENES


BOTONES = []


def mostrar_textos(pantalla:pygame)->None:
    """
    muestra el titulo "BUSCAMINAS" en el menu
    ENTRADA:
    pantalla:pygame, donde se dibuja el texto
    SALIDA:
    none
    """
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


def pantalla_menu(pantalla:pygame)->None:
    """
    muestra el menu principal

    ENTRADA:
    pantalla: pygame, dibde se dibuja todo el menu
    SALIDA:
    none
    """
    # Escala la imagen de fondo al tamaño pantalla
    imagen_fondo = pygame.transform.scale(IMAGENES["fondo"], (pantalla.get_width(), pantalla.get_height()))
    pantalla.blit(imagen_fondo, (0, 0))

    mostrar_textos(pantalla)
    dibujar_botones(pantalla)


def dibujar_botones(pantalla:pygame)->None:
    """
    dibuja los botones del menu principal en la pantalla

    ENTRADA:
    pantalla:pygame, donde se dibujan los botones
    SALIDA:
    none
    """
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

def manejar_click(pos:tuple[int,int], estado_juego:dict)->None:
    """
    detecta si el click fue sobre algun boton
    ENTRADA:
    pos:tupla con la posicion (X,y) del click del mouse
    estado_juego: dict con el estado actual del juego
    SALIDA:
    none
    """
    for i in range(len(BOTONES)):
        if BOTONES[i].collidepoint(pos):
            ejecutar_funcion(i, estado_juego)

def ejecutar_funcion(indice:int, estado_juego:dict)-> None:
    """
    ejecuta la accion segun el rectangulo clickeado

    ENTRADA:
    indice:int, indica la accion a ejecutar
    estado_juego: dict con el estado actual del juego
    SALIDA:
    none 
    """
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

def jugar(estado_juego:dict)-> None:
    """
    prepara el juego para empezar

    ENTRADA:
    estado_juego: dict con el estado actual del juego
    SALida:
    NONE
    """
    # estado_juego.clear()
    estado_juego["juego_iniciado"] = False
    estado_juego["perdio"] = False
    configuraciones.set_pantalla_actual("juego")




def ver_puntajes(estado_juego:dict)-> None:
    """
    cambia la pantalla actual a la pantalla de los puntajes
    ENTRADA:
    estado_juego: dict con el estado actual del juego
    SALIDA:
    si salida
    """
    configuraciones.set_pantalla_actual("puntaje")

def salir():
    """
    cierra el pygame y termina el programa
    ENTRADA:
    ninguna
    SALIDA:
    ninguna(finaliza la ejecucion)
    """
    pygame.quit()
    exit()
