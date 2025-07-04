import pygame
# ruta_imagenes = 'imagenes/'
# imagen_celda = pygame.image.load(f"{ruta_imagenes}bloque-vacio")
# imagen_celda = pygame.transform.scale(imagen_celda, 120, 120)
# rect_celda = pygame.Rect(50,50, 100,100)

TAM_CELDA = 40
MARGEN = 1



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
    "8": pygame.image.load("imagenes/8.png")
}

for nombre_img,img_superficie in IMAGENES.items():
    IMAGENES[nombre_img] = pygame.transform.scale(img_superficie,(TAM_CELDA, TAM_CELDA))


def inicializar_react_celdas(tablero, pantalla, margen, tam_celda, ancho_tablero, alto_tablero):
    offset_x = (pantalla.get_width() - ancho_tablero) // 2
    offset_y = (pantalla.get_height() - alto_tablero) // 2
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            x = offset_x + margen + columna * (tam_celda + margen)
            y = offset_y + margen + fila * (tam_celda + margen)
            tablero[fila][columna]["rect"] = pygame.Rect(x, y, tam_celda, tam_celda)



def dibujar_tablero(pantalla, tablero, imagenes, juego_perdido):
    for fila in tablero:
        for celda in fila:
            if celda["rect"]:
                imagen_celda = ""
                if celda["estado"] == True:
                    imagen_celda = celda["valor"]
                else:
                    if juego_perdido and celda["valor"] == "bomba":
                        imagen_celda = "bomba" # Mostrar bombas cuando se pierde
                    else:
                        imagen_celda = "bloque-vacio" # De lo contrario, es un bloque oculto
                imagen = pygame.transform.scale(imagenes[imagen_celda], (celda["rect"].width, celda["rect"].height))
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


    if evento is not None and evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        if rect_volver.collidepoint(evento.pos):
            return True
    return False

def calcular_tamanio_celda(filas, columnas, max_ancho, max_alto, margen):
    tam_ancho = (max_ancho - (columnas + 1) * margen) // columnas
    tam_alto = (max_alto - (filas + 1) * margen) // filas
    return min(tam_ancho, tam_alto)


