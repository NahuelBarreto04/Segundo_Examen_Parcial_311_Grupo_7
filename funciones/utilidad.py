import pygame
# ruta_imagenes = 'imagenes/'
# imagen_celda = pygame.image.load(f"{ruta_imagenes}bloque-vacio")
# imagen_celda = pygame.transform.scale(imagen_celda, 120, 120)
# rect_celda = pygame.Rect(50,50, 100,100)

TAM_CELDA = 40
MARGEN = 1



IMAGENES = {
    "bloque-vacio.png": pygame.image.load("imagenes/bloque-vacio.png"),
    "bomba.png": pygame.image.load("imagenes/bomba.png"),
    "bandera.png": pygame.image.load("imagenes/bandera.png"),   
    "0.png": pygame.image.load("imagenes/0.png"), 
    "1.png": pygame.image.load("imagenes/1.png"),
    "2.png": pygame.image.load("imagenes/2.png"),
    "3.png": pygame.image.load("imagenes/3.png"),
    "4.png": pygame.image.load("imagenes/4.png"),
    "5.png": pygame.image.load("imagenes/5.png"),
    "6.png": pygame.image.load("imagenes/6.png"),
    "7.png": pygame.image.load("imagenes/7.png"),
    "8.png": pygame.image.load("imagenes/8.png")
}
#separa el key y el value de los items
for nombre_img,img_superficie in IMAGENES.items():
    IMAGENES[nombre_img] = pygame.transform.scale(img_superficie,(TAM_CELDA, TAM_CELDA))


def inicializar_react_celdas(tablero:list, pantalla, MARGEN, TAM_CELDA, ANCHO_TABLERO, ALTO_TABLERO):
    offset_x = (pantalla.get_width() - ANCHO_TABLERO) // 2
    offset_y = (pantalla.get_height() - ALTO_TABLERO) // 2
    for fila in range (len(tablero)):
        for columna in range(len(tablero[fila])):
            #calcular las posiciones
            x = offset_x + MARGEN + columna * (TAM_CELDA + MARGEN)
            y = offset_y + MARGEN + fila * (TAM_CELDA + MARGEN)
            #poner el react en el diccionario de la celda
            tablero[fila][columna]["rect"] = pygame.Rect(x,y, TAM_CELDA, TAM_CELDA)


def dibujar_tablero(pantalla, tablero, IMAGENES):
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            celda = tablero[fila][columna]
            if celda["rect"]:
                pygame.draw.rect(pantalla,(200,200,200), celda["rect"])

                imagen = IMAGENES[celda["valor"]]
                pantalla.blit(imagen, celda["rect"])
            
def dibujar_boton_volver(pantalla, evento):
    fuente = pygame.font.SysFont("arial", 25)
    texto = fuente.render("volver al menu", True, (255, 255, 255))
    ancho = texto.get_width() + 20
    alto = texto.get_height() + 10
    x = 20
    y = pantalla.get_height() - alto - 10
    rect_volver = pygame.Rect(x, y, ancho, alto)

    pygame.draw.rect(pantalla, (80, 80, 80), rect_volver)
    pantalla.blit(texto, (x + 10, y + 5))

    if evento != None and evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        if rect_volver.collidepoint(evento.pos):
            return True
    return False