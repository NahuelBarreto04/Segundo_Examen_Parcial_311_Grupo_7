import pygame
import random
# import configuraciones
from .utilidad import MARGEN, TAM_CELDA

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

def generar_minas(tablero: list, minas: int, fila_click: int, columna_click: int, estado_juego:dict):
    estado_juego["primera_celda"] = False
    cant_minas = minas
    primer_fila = 0
    primer_columna = 0

    while cant_minas > 0:
        fila = randint(0, len(tablero)- 1)
        columna = randint(0, len(tablero[0])- 1)
        if estado_juego["primera_celda"] == False:
            # print(primer_fila, primer_columna, "test")
            primer_fila = fila_click
            primer_columna = columna_click
            estado_juego["primera_celda"] = True
            continue

        if fila == primer_fila and columna == primer_columna:
            continue

        if tablero[fila][columna]["valor"] == "bloque-vacio":
            tablero[fila][columna]["valor"] = "bomba"
            tablero[fila][columna]["estado"] = False
            cant_minas -= 1




def obtener_fila_columna(pos, tablero):
    x, y = pos
    for f in range(len(tablero)):
        for c in range(len(tablero[0])):
            if tablero[f][c]["rect"].collidepoint(x, y):
                return f, c
    return -1, -1




#Calculo de numeros ad
def calcular_numeros(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])

    for r in range(filas):
        for c in range(columnas):
            if tablero[r][c]["valor"] == "bomba":
                continue # Saltar las bombas

            count = 0
            # Comprobar los 8 vecinos
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue # Salta la celda actual

                    nr, nc = r + dr, c + dc
                    if 0 <= nr < filas and 0 <= nc < columnas:
                        if tablero[nr][nc]["valor"] == "bomba":
                            count += 1
            tablero[r][c]["valor"] = str(count) # guarda como string para la imagen






def revelar_celda(estado_juego, fila, columna):
    tablero = estado_juego["tablero"]
    
    if not (0 <= fila < len(tablero) and 0 <= columna < len(tablero[0])):
        return None

    celda = tablero[fila][columna]

    if celda["estado"] == True:
        return None

    # 3. Si es una BOMBA
    if celda["valor"] == "bomba":
        celda["valor"] = "bomba_explosion" # Cambiamos a la imagen de explosión
        celda["estado"] = True            # La marcamos como revelada
        return "perdiste"                 # Indicamos que el juego ha terminado

    # 4. Si no es una bomba y no está revelada:
    celda["estado"] = True 

    #si la celda revelada es '0' (vacía)
    # revela sus 8 vecinos.
    if celda["valor"] == "0":
        for df in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if df == 0 and dc == 0:
                    continue #Salta la celda actual

                # Llamada recursiva para revelar los vecinos
                # La recursión continuará solo si los vecinos también son '0'
                revelar_celda(estado_juego, fila + df, columna + dc)
    

    return None


    





