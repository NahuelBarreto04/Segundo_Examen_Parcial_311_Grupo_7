import pygame


TAM_CELDA = 40
MARGEN = 1

SONIDOS = {
    "musica_menu": "sonidos/musica_menu.mp3",
    "musica_puntajes":"sonidos/musica_puntajes.mp3",
    "sonido_derrota": "sonidos/derrota.mp3",
    "sonido_victoria":"sonidos/victoria.mp3"
}

IMAGENES = {
    "bloque-vacio": pygame.image.load("imagenes/bloque-vacio.png"),
    "bomba": pygame.image.load("imagenes/bomba.png"),
    "bomba_explosion": pygame.image.load("imagenes/bomba_explosion.png"),
    "bandera": pygame.image.load("imagenes/bandera.png"),
    "0": pygame.image.load("imagenes/0.png"), 
    "1": pygame.image.load("imagenes/1.png"),
    "2": pygame.image.load("imagenes/2.png"),
    "3": pygame.image.load("imagenes/3.png"),
    "4": pygame.image.load("imagenes/4.png"),
    "5": pygame.image.load("imagenes/5.png"),
    "6": pygame.image.load("imagenes/6.png"),
    "7": pygame.image.load("imagenes/7.png"),
    "8": pygame.image.load("imagenes/8.png"),
    "cara": pygame.image.load("imagenes/cara.png"),
    "cara1": pygame.image.load("imagenes/cara1.png"),
    "cara2": pygame.image.load("imagenes/cara2.png"),
    "fondo_puntajes": pygame.image.load("imagenes/fondos/fondo_puntajes.jpg"),
    # "fondo_menu": pygame.image.load("imagenes/fondos/fondo_menu.png"),
    "8": pygame.image.load("imagenes/8.png"),
    "fondo": pygame.image.load("imagenes/fondo.jpg"),


}

for nombre_img,img_superficie in IMAGENES.items():
    """for para escalar las imagenes al tamaño de la celda """
    if "bloque" in nombre_img or "bomba" in nombre_img or "bandera" in nombre_img or nombre_img.isdigit():
        IMAGENES[nombre_img] = pygame.transform.scale(img_superficie,(TAM_CELDA, TAM_CELDA))
for nombre_img in IMAGENES:
    if nombre_img != "fondo":
        img_superficie = IMAGENES[nombre_img]
        IMAGENES[nombre_img] = pygame.transform.scale(img_superficie,(TAM_CELDA, TAM_CELDA))



def inicializar_react_celdas(tablero: list, pantalla, margen:int, tam_celda:int, ancho_tablero: int, alto_tablero:int)-> None:
    """Funcion inicializa el rect de las celdas y lo guarda en un key propia
    
    ENTRADA:
    tablero: lista
    pantalla: pantalla de pygame
    margen: Int
    tam_celda: int
    ancho_tablero: int 
    alto_tablero: int
    
    Salida:
    sin salida, funcion de modificación
    
    """

    offset_x = (pantalla.get_width() - ancho_tablero) // 2
    offset_y = (pantalla.get_height() - alto_tablero) // 2
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            x = offset_x + margen + columna * (tam_celda + margen)
            y = offset_y + margen + fila * (tam_celda + margen)
            tablero[fila][columna]["rect"] = pygame.Rect(x, y, tam_celda, tam_celda)



def dibujar_tablero(pantalla:pygame, tablero:list, imagenes:dict, juego_perdido:bool) -> None:
    """
    Funcion para dibujar el tablero del juego a partir de sus celdas y valores

    ENTRADA:
    pantalla: pantalla de pygame para modificaciones con la pantalla
    tablero: lista
    imagenes: diccionario con la carga de imagenes
    juego_perdido: booleano que indica si el juego esta perdido o no

    Salida:
    sin salida, funcion para mostrar con pygame
    """
    for fila in tablero:
        for celda in fila:
            if celda["rect"]:
                if celda.get("bandera") == True:
                    imagen_celda = "bandera"
                else:
                    if celda["estado"] == True:
                        imagen_celda = celda["valor"]
                    else:
                        if juego_perdido and celda["valor"] == "bomba":
                            imagen_celda = "bomba"  # Mostrar bombas cuando se pierde
                        else:
                            imagen_celda = "bloque-vacio"  # Bloque oculto
                imagen = pygame.transform.scale(imagenes[imagen_celda], (celda["rect"].width, celda["rect"].height))
                pantalla.blit(imagen, celda["rect"])



            
def dibujar_boton_volver(pantalla:pygame, evento:pygame) -> None:
    """
    Funcion del boton para regresar a la pantalla anterior

    ENTRADA:
    pantalla: pantalla de pygame 
    evento: eventos pygame para manejar el click
    SALIDA:
    True: porque el evento colisiono con el boton
    False: el evento no colisiono con la posicion del boton
    """
    fuente = pygame.font.SysFont("arial", 25)
    texto = fuente.render("volver al menu", True, (255, 255, 255))
    ancho = texto.get_width() + 20
    alto = texto.get_height() + 10
    x = 20
    y = pantalla.get_height() - alto - 10
    rect_volver = pygame.Rect(x, y, ancho, alto)


    pygame.draw.rect(pantalla, (80, 80, 80), rect_volver)
    pantalla.blit(texto, (x + 10, y + 5))


    if evento is not None and evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        if rect_volver.collidepoint(evento.pos):
            return True
    return False



