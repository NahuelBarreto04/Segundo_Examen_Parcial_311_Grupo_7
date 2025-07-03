import pygame
#Archivos de configuracion_juegoes
#DICCIONARIO DE CONFIGURACION
configuracion_juego = {
    "tablero": [],
    "resolucion_actual": "800x600",
    "dificultad_actual": "facil",
    "pantalla_actual": "menu",
    "PANTALLA:": None
}

dificultad_juego = {}

#React Pantalla
def set_pantalla_pygame(pantalla):
    """Establece la Pantalla pygame"""
    configuracion_juego["PANTALLA"] = pantalla

def get_pantalla_pygame():
    return configuracion_juego["PANTALLA"]


#Resolución
def get_resolucion_actual():
    partes = configuracion_juego["resolucion_actual"].split("x")
    ancho = int(partes[0])
    alto = int(partes[1])
    return ancho, alto

def set_resolucion_actual(valor): 
    configuracion_juego["resolucion_actual"] = valor
    print(f"Nueva resolución: {configuracion_juego["resolucion_actual"]}")

    if configuracion_juego["PANTALLA"]:
        ancho,alto = get_resolucion_actual()
        configuracion_juego["PANTALLA"] = pygame.display.set_mode((ancho, alto), pygame.SCALED)

def cambiar_resolucion():
    """Alterna entre las resoluciones predefinidas."""
    if configuracion_juego["resolucion_actual"] == "800x600":
        set_resolucion_actual("1024x768")
    elif configuracion_juego["resolucion_actual"] == "1024x768":
        set_resolucion_actual("620x480")
    else:
        set_resolucion_actual("800x600")



#DIFICULTAD
def get_dificultad_actual():
    """Devuelve la dificultad actual."""
    return configuracion_juego["dificultad_actual"]

def set_dificultad_actual(dificultad):
    configuracion_juego["dificultad_actual"] = dificultad

def cambiar_dificultad():
    """Alterna entre las dificultades: fácil, normal, difícil."""
    if configuracion_juego["dificultad_actual"] == "facil":
        configuracion_juego["dificultad_actual"] = "normal"
    elif configuracion_juego["dificultad_actual"] == "normal":
        configuracion_juego["dificultad_actual"] = "dificil"
    else:
        configuracion_juego["dificultad_actual"] = "facil"



#Pantalla actual
def get_pantalla_actual():
    return configuracion_juego["pantalla_actual"]

def set_pantalla_actual(pantalla_actual):
    configuracion_juego["pantalla_actual"] = pantalla_actual





