import pygame
import random
from .utilidad import SONIDOS

randint = random.randint

CELDA = {
    "valor": "bloque-vacio",
    "rect": "",
    "estado": False}


def generar_tablero(filas:int, columnas:int, valor:any) -> list:
    """
    genera un tablero como una matriz de celdas
    crea una lista con la cantidad de filas y columnas
    ENTRADA:
    filas: int cantidad de filas
    columnas int cantidad de columnas
    valor: alguno 
    SALIDA:
    devuelve el tablero generado

    """
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            celda = valor.copy()
            fila.append(celda)
        tablero.append(fila)
    return tablero


def mostrar_tablero(tablero:list) -> None:
    """
    muestra por consola los valores del tablero
    recorre cada fila y columna de este 
    y muestra el valor de cada celda

    ENTRADA: 
    tablero: lista matriz del juego
    SALIDA:
    Sin salida
    """
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j]["valor"], end=" ")
        print("")
    print(" ")




def generar_minas(tablero:list, minas:int, fila_click: int, columna_click:int) -> None:
    """fncion para generar las minas en el tablero
    
    ENTRADA:
    tablero: lista tablero del juego
    minas: int cantidad de minas
    fila_click: int numero de fila
    columna_click: int numero de columna
    SALIDA:
    Sin salida
    """
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
                    tablero[fila][columna]["estado"] = True
                    cant_minas -= 1






def obtener_fila_columna(pos:pygame, tablero:list) -> int:
    """funcion para obtener fila y columna del click
    
    ENTRADA: 
    pos: posicion del evento
    tablero: lista tablero del juego
    """

    x, y = pos
    for f in range(len(tablero)):
        for c in range(len(tablero[0])):
            if tablero[f][c]["rect"].collidepoint(x, y):
                return f, c
    return -1, -1




#Calculo de numeros ad
def calcular_numeros(tablero:list) -> None:
    """Funcion para calcular y encontrar los numeros adyacentes
    
    ENTRADA:
    tablero: lista tablero del juego
    SALIDA:
    Sin salida
    
    """

    filas = len(tablero)
    columnas = len(tablero[0])

    for f in range(filas):
        for c in range(columnas):
            if tablero[f][c]["valor"] == "bomba":
                continue # Saltar las bombas

            count = 0
            # para buscar en las celdas de al lado
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue # Salta la celda actual

                    nr, nc = f + dr, c + dc
                    if 0 <= nr < filas and 0 <= nc < columnas:
                        if tablero[nr][nc]["valor"] == "bomba":
                            count += 1
            tablero[f][c]["valor"] = str(count) # guarda como string para la imagen






def revelar_celda(estado_juego:dict, fila:int, columna:int) -> str|None:
    """
    revela una celda del tablero 
    -si la celda esta fuera del tablero no hace nada
    -si ya fue revela o tiene una bandera no hace nada
    -si es una bomba,marca que exploto y devuelve "perdiste"
    -si es una celda vacia ("0"), revela tmb sus celdas vecinas
    
    si releva una bomba devuelve "perdiste"
    en los otros casos, no devuelve none

    ENTRADA:
    estado_juego: diccionario
    SALIDA:
    Sin salida

    """
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
    #busca las vacias alrededor
    if celda["valor"] == "0":
        for df in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if df == 0 and dc == 0:
                    continue
                revelar_celda(estado_juego, fila + df, columna + dc)

    return None



def verificar_ganador(estado_juego:dict) -> bool:
    """
    verifica si el usuario gano el juego
    recorre todas las celdas del tablero y si

    -encuentra una celda vacia que no es bomba y que no fue revelada,
    retorna false

    -si todas las celdas sin bombas fueron reveladas,
    retorna true
    """
    tablero = estado_juego["tablero"]
    for fila in tablero:
        for celda in fila:
            if celda["valor"] != "bomba" and celda["estado"] == False:
                return False
    return True

def resetear_juego(estado_juego:dict)-> None:
    """
    reinicia el juego y su estado del juego para iniciar un nuevo juego

    ENTRADA:
    estado_juego: diccionario 
    """
    estado_juego["juego_iniciado"] = False
    estado_juego["perdio"] = False
    estado_juego["minas_generadas"] = False




def calcular_puntaje(dificultad:str, tiempo:int) -> int:
    """
    calcula el puntaje dependiendo la dificultad

    -por cada segundo resta 10 puntos
    -el puntaje no puede ser menor a 0
    -retorna puntaje

    ENTRADA:
    dificultad: string 
    tiempo: int tiempo que va en el juego
    """
    if dificultad == "facil":
        base = 1000
    elif dificultad == "normal":
        base = 5000
    else: #dificil
        base = 10000

    puntaje = base - tiempo * 10
    if puntaje < 0:
        puntaje = 0
    return puntaje

def reproducir_musica(nombre_musica: str,estado_jugo: dict) -> None:
    """
    reproduce la musica segun el nombre indicado

    -Si el nombre es "No", la musica se detiene
    -Si la musica actual es distinta, se carga y se reproduce la nueva
    -guarda el nombre de la musica actual en el diccionario del estado
    -ajusta el  volumen a 0.5

    ENTRADA:
    nombre_musica: string nombre de la musica
    estado_jugo: diccionario que maneja los estado del juego
    Salida:
    Sin salida
    """
    if(nombre_musica == "No"):
        estado_jugo["musica_actual"] = "No"
        pygame.mixer.music.stop()
    elif estado_jugo["musica_actual"] != nombre_musica:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(SONIDOS[nombre_musica])
        pygame.mixer.music.play(-1) 
        pygame.mixer.music.set_volume(0.5)
        estado_jugo["musica_actual"] = nombre_musica

def reproducir_sonido(nombre_sonido: str) -> None:
    """
    reproduce un sonido segun el nombre recibido
    lo busca desde el diccionario de sonidos 
    lo carga como sonido y lo reproduce 1 vez

    ENTRADA:
    nombre_sonido: string nombre del sonido
    SALIDA:
    Sin salida
    """
    sonido = pygame.mixer.Sound(SONIDOS[nombre_sonido])
    sonido.play()


