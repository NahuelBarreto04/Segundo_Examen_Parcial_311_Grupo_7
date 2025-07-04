import pygame
import random
# import configuraciones
from .utilidad import MARGEN, TAM_CELDA,SONIDOS

randint = random.randint

CELDA = {
    "valor": "bloque-vacio",
    "rect": "",
    "estado": False}


def generar_tablero(filas:int, columnas:int, valor:any):
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            celda = valor.copy()
            fila.append(celda)
        tablero.append(fila)
    return tablero


def mostrar_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j]["valor"], end=" ")
        print("")
    print(" ")



def obtener_fila_columna(pos, tablero):
    x, y = pos
    for f in range(len(tablero)):
        for c in range(len(tablero[0])):
            if tablero[f][c]["rect"].collidepoint(x, y):
                return f, c
    return -1, -1

def generar_minas(tablero, minas, fila_click, columna_click, estado_juego):
    cant_minas = minas
    primera_vez = True

    while cant_minas > 0:
        fila = randint(0, len(tablero) - 1)
        columna = randint(0, len(tablero[0]) - 1)

        if primera_vez == True:
            primera_vez = False
        else:
            # Solo si está fuera del area 3x3 alrededor del click
            if fila < fila_click - 1 or fila > fila_click + 1 or columna < columna_click - 1 or columna > columna_click + 1:
                if tablero[fila][columna]["valor"] == "bloque-vacio":
                    tablero[fila][columna]["valor"] = "bomba"
                    tablero[fila][columna]["estado"] = False
                    cant_minas -= 1






def obtener_fila_columna(pos, tablero:list) -> int:
    x, y = pos
    for f in range(len(tablero)):
        for c in range(len(tablero[0])):
            if tablero[f][c]["rect"].collidepoint(x, y):
                return f, c
    return -1, -1




#Calculo de numeros ad
def calcular_numeros(tablero:list) -> None:
    filas = len(tablero)
    columnas = len(tablero[0])

    for f in range(filas):
        for c in range(columnas):
            if tablero[f][c]["valor"] == "bomba":
                continue # Saltar las bombas

            count = 0
            # Comprobar los 8 vecinos
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue # Salta la celda actual

                    nr, nc = f + dr, c + dc
                    if 0 <= nr < filas and 0 <= nc < columnas:
                        if tablero[nr][nc]["valor"] == "bomba":
                            count += 1
            tablero[f][c]["valor"] = str(count) # guarda como string para la imagen






def revelar_celda(estado_juego, fila, columna) -> bool:
    tablero = estado_juego["tablero"]
    
    if not (0 <= fila < len(tablero) and 0 <= columna < len(tablero[0])):
        return None

    celda = tablero[fila][columna]

    # No revelar si ya tiene bandera
    if celda.get("bandera") == True:
        return None

    if celda["estado"] == True:
        return None

    if celda["valor"] == "bomba":
        celda["valor"] = "bomba_explosion"
        celda["estado"] = True
        return "perdiste"

    celda["estado"] = True

    if celda["valor"] == "0":
        for df in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if df == 0 and dc == 0:
                    continue
                revelar_celda(estado_juego, fila + df, columna + dc)

    return None



def verificar_ganador(estado_juego:dict) -> bool:
    tablero = estado_juego["tablero"]
    for fila in tablero:
        for celda in fila:
            if celda["valor"] != "bomba" and celda["estado"] == False:
                return False
    return True



def resetear_juego(estado_juego:dict):
    estado_juego["juego_iniciado"] = False
    estado_juego["perdio"] = False
    estado_juego["minas_generadas"] = False



def reproducir_musica(nombre_musica: str,estado_jugo: dict):
    if estado_jugo["musica_actual"] != nombre_musica:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(SONIDOS[nombre_musica])
        pygame.mixer.music.play(-1) 
        pygame.mixer.music.set_volume(0.5)
        estado_jugo["musica_actual"] = nombre_musica