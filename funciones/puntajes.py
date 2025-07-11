import pygame
import pygame
from .utilidad import IMAGENES, dibujar_boton_volver, SONIDOS
from .configuraciones import *
import csv
import os

ARCHIVO_PUNTAJES = "./puntajes.csv"

def pantalla_puntajes(pantalla, evento, estado_juego: dict):
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




def guardar_puntaje(nombre_jugador, puntaje) -> None:
    """
    Funcion para guardar el puntaje en el archivo CSV. 
    Si el nombre ya existe, conserva el mayor puntaje.
    """
    puntajes = cargar_puntajes()

    existe = False
    for jugador in puntajes:
        if jugador[0].lower() == nombre_jugador.lower():
            existe = True
            if puntaje > jugador[1]:
                jugador[1] = puntaje
            break
    
    if not existe:
        puntajes.append([nombre_jugador, puntaje])

    puntajes.sort(key=obtener_puntaje, reverse=True)
    puntajes = puntajes[:10]
    
    with open(ARCHIVO_PUNTAJES, "w", encoding="utf-8") as archivo:
        archivo.write("nombre,puntaje\n")  # Escribir encabezados
        for jugador in puntajes:
            archivo.write(f"{jugador[0]},{jugador[1]}\n")


def obtener_puntaje(jugador) -> int:
    """Funcion para obtener el puntaje del jugador"""
    return jugador[1]

def cargar_puntajes():
    """Cargar la lista de puntajes del archivo csv puntajes"""
    if not os.path.exists(ARCHIVO_PUNTAJES):
        return []
    
    puntajes = []
    with open(ARCHIVO_PUNTAJES, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            valores = linea.split(",")
            linea = linea.strip()
            
            nombre = valores[0].strip()
            puntaje = int(valores[1])
            puntajes.append([nombre, puntaje])
    print(puntajes)
    return puntajes


def mostrar_puntaje(pantalla):
    """
    Funcion para mostrar jugadores y puntajes en lista en la pantalla puntajes
    """
    print(pantalla)
    fuente_puntajes = pygame.font.SysFont("Arial", 32)
    puntajes = cargar_puntajes()
    print(puntajes)
    for i in range(len(puntajes)):
        texto = f"{i+1}:{puntajes[i][0]}: {puntajes[i][1]}"
        print(texto)
        render_texto = fuente_puntajes.render(texto, True,(255, 255, 255))
        y_pos = 130
        pantalla.blit(render_texto, (pantalla.get_width()//2 - render_texto.get_width()//2, y_pos))
        y_pos += 20


def dibujar_victoria(pantalla) -> None:
    """
    Funcion para dibujar el texto de victoria y puntaje en pantalla una vez que el jugador gane
    """
    fuente = pygame.font.SysFont("arial", 60, bold=True)
    texto = fuente.render("GANASTE!", True, (0, 255, 0))
    sombra = fuente.render("GANASTE!", True, (0, 0, 0))

    x = (pantalla.get_width() - texto.get_width()) // 2
    y = pantalla.get_height() // 2 - texto.get_height() // 2

    fondo_rect = pygame.Rect(x - 20, y - 20, texto.get_width() + 40, texto.get_height() + 40)
    pygame.draw.rect(pantalla, (20, 20, 20), fondo_rect, border_radius=15)

    pantalla.blit(sombra, (x + 3, y + 3))
    pantalla.blit(texto, (x, y))
