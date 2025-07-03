import pygame
#from funciones.menu import mostrar_textos, dibujar_botones, manejar_click, get_pantalla_actual, set_pantalla_actual, dificultad_actual,pantalla_actual
from funciones.pantallas import *
from funciones.menu import *
from funciones.funciones import revelar_celda
from funciones import *




pygame.init()
pygame.font.init()
pygame.display.set_caption("Buscaminas")

COLOR_FONDO = (54, 54, 54)
ANCHO_INICIAL, ALTO_INICIAL = configuraciones.get_resolucion_actual()
PANTALLA = pygame.display.set_mode((ANCHO_INICIAL, ALTO_INICIAL), pygame.SCALED)
configuraciones.set_pantalla_pygame(PANTALLA)
inicio_timer = None

def pantalla_menu():
    PANTALLA = configuraciones.get_pantalla_pygame()
    PANTALLA.fill(COLOR_FONDO)
    print(PANTALLA)
    mostrar_textos(PANTALLA)
    dibujar_botones(PANTALLA)
    pygame.display.flip()

estado_juego = {"juego_iniciado": False}

def menu_interaccion():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

            if configuraciones.get_pantalla_actual() == "menu":
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    manejar_click(evento.pos)
                pantalla_menu()

            elif configuraciones.get_pantalla_actual() == "juego":

                if estado_juego["juego_iniciado"] == False:
                    iniciar_juego(configuraciones.get_pantalla_pygame(), estado_juego)
                    estado_juego["minas_generadas"] = False

                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    fila, col = obtener_fila_columna(evento.pos, estado_juego["tablero"])
                    if estado_juego.get("minas_generadas") == False:
                        generar_minas_asegurando_celda_segura(estado_juego["tablero"], estado_juego["minas"], fila, col)
                        estado_juego["minas_generadas"] = True
                    revelar_celda(estado_juego["tablero"], fila, col)



                dibujar_juego(configuraciones.get_pantalla_pygame(), evento, estado_juego)


        if configuraciones.get_pantalla_actual() == "juego" and estado_juego.get("juego_iniciado") == True:
            dibujar_juego(configuraciones.get_pantalla_pygame(), None, estado_juego)








            #inicio_timer = pantalla_juego(PANTALLA,evento,inicio_timer)
        

# actualizar_resolucion()
menu_interaccion()