# import pygame
import random

randint = random.randint

CELDA = {
    "valor": 0,
    "rect": "",
    "estado": True
}

BOMBA = {
    "valor": 1,
    "rect": "",
    "estado": True
}

def generar_tablero(filas:int, columnas:int, valor:any):
    tablero = []
    for i in range(filas):
        fila = [valor] * columnas
        tablero += [fila]
    return tablero

tablero = (generar_tablero(8,8,CELDA))
print(len(tablero))
def mostrar_tablero(tablero):
    # print(tablero)
    for i in range(len(tablero)):
        print("")
        for x in range(len(tablero[i])):
            print(tablero[i][x]["valor"], end=" ")
    print(" ")
           
mostrar_tablero(tablero)


def generar_minas(tablero: list, cant_minas: int, BOMBA:dict):
    while cant_minas > 0:
        fila = randint(0, len(tablero)- 1)
        columna = randint(0, len(tablero[0])- 1)
        if tablero[fila][columna]["valor"] == 0:
            tablero[fila][columna] = BOMBA
            cant_minas -= 1

# # print(tablero)
generar_minas(tablero, 8, BOMBA)
mostrar_tablero(tablero)


