import pygame
import random
import configuraciones
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

iniciacializar_tablero()

# def dibujar_tablero(tablero:list):
    





