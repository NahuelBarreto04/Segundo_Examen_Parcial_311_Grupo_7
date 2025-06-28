import pygame
# ruta_imagenes = 'imagenes/'
# imagen_celda = pygame.image.load(f"{ruta_imagenes}bloque-vacio")
# imagen_celda = pygame.transform.scale(imagen_celda, 120, 120)
# rect_celda = pygame.Rect(50,50, 100,100)

TAM_CELDA = 40
MARGEN = 1

FILAS = 8
COLUMNAS = 8

ANCHO_TABLERO = COLUMNAS * (TAM_CELDA + MARGEN) + MARGEN
ALTO_TABLERO = FILAS * (TAM_CELDA + MARGEN) + MARGEN

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



