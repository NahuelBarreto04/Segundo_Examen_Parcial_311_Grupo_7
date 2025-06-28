# import pygame
import random

randint = random.randint

CELDA = {
    "valor": "bloque-vacio.png",
    "rect": "",
    "estado": False
}

# BOMBA = {
#     "valor": 1,
#     "rect": "",
#     "estado": True
# }

def generar_tablero(filas:int, columnas:int, valor:any):
    tablero = []
    for i in range(filas):
        fila = []
        for x in range(columnas):
            celda = valor.copy()
            fila.append(celda)
        tablero.append(fila)
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
           
# mostrar_tablero(tablero)


def generar_minas(tablero: list, minas: int, BOMBA:dict):
    cant_minas = minas
    while cant_minas > 0:
        fila = randint(0, len(tablero)- 1)
        columna = randint(0, len(tablero[0])- 1)
        if tablero[fila][columna]["valor"] == "bloque-vacio.png":
            tablero[fila][columna]["valor"] = "bomba.png"
            cant_minas -= 1
            print(cant_minas)


# print(tablero)
# # mostrar_tablero(tablero)
# generar_minas(tablero, 5, CELDA)
# mostrar_tablero(tablero)


