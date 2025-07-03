import pygame
import random
import configuraciones
from .utilidad import MARGEN, TAM_CELDA

randint = random.randint

CELDA = {
    "valor": "bloque-vacio.png",
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
    # print(tablero)
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j]["valor"], end=" ")
        print("")
    print(" ")

tablero = generar_tablero(8,8,CELDA)      
mostrar_tablero(tablero)


def generar_minas(tablero: list, minas: int, BOMBA:dict):
    cant_minas = minas
    while cant_minas > 0:
        fila = randint(0, len(tablero)- 1)
        columna = randint(0, len(tablero[0])- 1)
        if tablero[fila][columna]["valor"] == "bloque-vacio.png":
            tablero[fila][columna]["valor"] = "bomba.png"
            cant_minas -= 1


configuraciones.dificultad_juego["filas"] = 16
configuraciones.dificultad_juego["columnas"] = 16
configuraciones.dificultad_juego["minas"] = 50
#Logica del Tablero
def iniciacializar_tablero(nueva_partida):
    tablero = []
    if nueva_partida:
        tablero = generar_tablero(configuraciones.dificultad_juego["filas"], configuraciones.dificultad_juego["columnas"], CELDA)
        generar_minas(tablero, configuraciones.dificultad_juego["minas"], CELDA)
        configuraciones.configuracion_juego["tablero"] = tablero 
        
def obtener_fila_columna(pos, tablero):
    x, y = pos
    for f in range(len(tablero)):
        for c in range(len(tablero[0])):
            if tablero[f][c]["rect"].collidepoint(x, y):
                return f, c
    return -1, -1


def generar_minas_asegurando_celda_segura(tablero, minas, fila_segura, col_segura):
    filas = len(tablero)
    columnas = len(tablero[0])
    minas_puestas = 0
    while minas_puestas < minas:
        f = random.randint(0, filas - 1)
        c = random.randint(0, columnas - 1)

        if f == fila_segura and c == col_segura:
            continue
        if tablero[f][c]["valor"] == "bloque-vacio.png":
            tablero[f][c]["valor"] = "bomba.png"
            minas_puestas += 1


def obtener_fila_columna(pos, tablero):
    x, y = pos
    for f in range(len(tablero)):
        for c in range(len(tablero[0])):
            if tablero[f][c]["rect"].collidepoint(x, y):
                return f, c
    return -1, -1


def revelar_celda(tablero, fila, columna):
    if fila < 0 or fila >= len(tablero):
        return
    if columna < 0 or columna >= len(tablero[0]):
        return

    celda = tablero[fila][columna]
    if celda["estado"] == True:
        return

    if celda["valor"] == "bomba.png":
        celda["valor"] = "bomba_explosion.png"
        celda["estado"] = True
        return "perdiste"

    celda["estado"] = True

    if celda["valor"] == "0.png":
        for df in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if df != 0 or dc != 0:
                    revelar_celda(tablero, fila + df, columna + dc)




iniciacializar_tablero()

# def dibujar_tablero(tablero:list):
    





