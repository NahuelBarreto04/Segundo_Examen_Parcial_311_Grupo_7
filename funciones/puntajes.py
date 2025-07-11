import pygame
import pygame
from .utilidad import IMAGENES, dibujar_boton_volver
from .configuraciones import *
import os

ARCHIVO_PUNTAJES = "./puntajes.csv"

def pantalla_puntajes(pantalla:pygame, evento:pygame) -> None:
    """
    Funcion para la muestra de la pantalla puntaje y lo necesario en su pantalla

    Entrada:
    pantalla: pantalla pygame
    evento: eventos pygame para manejar el evento
    """

    fondo = pygame.transform.scale(IMAGENES["fondo_puntajes"], pantalla.get_size())
    pantalla.blit(fondo, (0, 0))

    fuente_titulo = pygame.font.SysFont("arial", 50)
    texto_titulo = fuente_titulo.render("Puntajes Altos", True, (255, 255, 255))
    rect_titulo = texto_titulo.get_rect(center=(pantalla.get_width() // 2, 100))
    pantalla.blit(texto_titulo, rect_titulo)

    mostrar_puntaje(pantalla)





    if dibujar_boton_volver(pantalla, evento): 
        set_pantalla_actual("menu")
    pygame.display.flip()




def guardar_puntaje(nombre_jugador, puntaje) -> None:
    """
    Funcion para guardar el puntaje en el archivo CSV. 
    Si el nombre ya existe, conserva el mayor puntaje.

    ENTRADA:
    nombre_jugador: string
    puntaje: string puntaje del jugador que ganó
    SALIDA:
    Sin salida
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

    puntajes.sort(key=obtener_puntaje, reverse= True)
    puntajes = puntajes[:10]
    
    with open(ARCHIVO_PUNTAJES, "w", encoding="utf-8") as archivo:
        # archivo.write("nombre,puntaje\n")  # Escribir encabezados
        for jugador in puntajes:
            archivo.write(f"{jugador[0]},{jugador[1]} \n")


def obtener_puntaje(jugador:list) -> int:
    """Funcion para obtener el puntaje del jugador
    ENTRADA:    
    jugador: lista que contiene nombre y puntaje 
    Salida:
    puntaje
    """
    return jugador[1]

def cargar_puntajes() -> list:
    """Cargar la lista de puntajes del archivo csv puntajes
    ENTRADA:
    Sin Entrada
    SALIDA:
    puntajes: lista con los puntajes del archivo
    
    """
    if not os.path.exists(ARCHIVO_PUNTAJES):
        return []
    
    puntajes = []
    with open(ARCHIVO_PUNTAJES, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        print(lineas)
        if len(lineas) < 1:
            return puntajes
        
        for linea in lineas:
            linea = linea.strip()
            valores = linea.split(",")
            nombre = valores[0].strip()
            puntaje = int(valores[1])
            puntajes.append([nombre, puntaje])

    return puntajes


def mostrar_puntaje(pantalla:pygame) -> None:
    """
    Funcion para mostrar jugadores y puntajes en lista en la pantalla puntajes
    ENTRADA:
    pantalla: pantalla pygame para mostrar datos
    """
    fuente_puntajes = pygame.font.SysFont("Arial", 32)
    puntajes = cargar_puntajes()
    y_pos = 130

    for i in range(len(puntajes)):
        texto = f"{i+1}:{puntajes[i][0]}: {puntajes[i][1]}"
        render_texto = fuente_puntajes.render(texto, True,(255, 255, 255))
        pantalla.blit(render_texto, (pantalla.get_width()//2 - render_texto.get_width()//2, y_pos))
        y_pos += 40



def dibujar_victoria(pantalla: pygame) -> None:
    """
    Funcion para dibujar el texto de victoria y puntaje en pantalla una vez que el jugador gane

    ENTRADA: 
    pantalla: pantalla pygame para mostrar
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
