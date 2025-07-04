import pygame
from funciones.pantallas import *
from funciones.menu import *
from funciones import *
from funciones.utilidad import IMAGENES, SONIDOS
from funciones.puntajes import *

pygame.init()
pygame.font.init()
pygame.display.set_caption("Buscaminas")
COLOR_FONDO = (54, 54, 54)
ANCHO_INICIAL, ALTO_INICIAL = configuraciones.get_resolucion_actual()
PANTALLA = pygame.display.set_mode((ANCHO_INICIAL, ALTO_INICIAL), pygame.SCALED)
configuraciones.set_pantalla_pygame(PANTALLA)

estado_juego = {
    "juego_iniciado": False,
    "perdio": False
}
mixer_config = pygame.mixer
mixer_config.init()
mixer_config.music.load(SONIDOS["musica_fondo"])
mixer_config.music.play(-1)
mixer_config.music.set_volume(0.05)




def pantalla_menu():
    pantalla = configuraciones.get_pantalla_pygame()
    pantalla.fill(COLOR_FONDO)
    # fondo = pygame.transform.scale(IMAGENES["fondo_menu"], pantalla.get_size())
    # pantalla.blit(fondo, (0, 0))
from funciones.utilidad import IMAGENES

def pantalla_menu():
    pantalla = configuraciones.get_pantalla_pygame()
    imagen_fondo = pygame.transform.scale(IMAGENES["fondo"], (pantalla.get_width(), pantalla.get_height()))
    pantalla.blit(imagen_fondo, (0, 0))
    mostrar_textos(pantalla)
    dibujar_botones(pantalla)
    pygame.display.flip()




#FUNCION PRINCIPAL

def menu_interaccion():
    reloj = pygame.time.Clock()

    while True:
        evento = None
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            evento = e

        if configuraciones.get_pantalla_actual() == "menu":
            if evento and evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                manejar_click(evento.pos, estado_juego)
                pantalla_actual = "menu"
                print(pantalla_actual)
            pantalla_menu()

        elif configuraciones.get_pantalla_actual() == "puntaje":
            pantalla_puntajes(configuraciones.get_pantalla_pygame(), evento)

        elif configuraciones.get_pantalla_actual() == "juego":
            if estado_juego["juego_iniciado"] == False:
                iniciar_juego(configuraciones.get_pantalla_pygame(), estado_juego)
                estado_juego["minas_generadas"] = False

        



            if evento and evento.type == pygame.MOUSEBUTTONDOWN:
                if estado_juego["perdio"] == False and estado_juego.get("gano") == False:
                    fila, col = obtener_fila_columna(evento.pos, estado_juego["tablero"])
                    print(fila, col)

                    if fila != -1 and col != -1:
                        if evento.button == 1:  # Click izquierdo
                            if estado_juego["minas_generadas"] == False:
                                generar_minas(estado_juego["tablero"], estado_juego["minas"], fila, col, estado_juego)
                                estado_juego["minas_generadas"] = True
                                calcular_numeros(estado_juego["tablero"])

                            if estado_juego["perdio"] == False:
                                resultado = revelar_celda(estado_juego, fila, col)
                                if resultado == "perdiste":
                                    estado_juego["perdio"] = True
                                    estado_juego["tiempo_final"] = (pygame.time.get_ticks() - estado_juego["inicio_timer"]) // 1000
                                else:
                                    if verificar_ganador(estado_juego):
                                        estado_juego["gano"] = True
                                        estado_juego["tiempo_final"] = (pygame.time.get_ticks() - estado_juego["inicio_timer"]) // 1000
                                        dificultad = configuraciones.get_dificultad_actual()
                                        tiempo = estado_juego["tiempo_final"]
                                        estado_juego["puntaje"] = calcular_puntaje(dificultad, tiempo)

                        elif evento.button == 3:  # Click derecho
                            celda = estado_juego["tablero"][fila][col]

    # SOLO si la celda NO esta revelada
                            if celda["estado"] == False:
                                if celda.get("bandera") == True:
                                    celda["bandera"] = False
                                    estado_juego["banderas_puestas"] -= 1
                                else:
                                    if estado_juego["banderas_puestas"] < estado_juego["minas"]:
                                        celda["bandera"] = True
                                        estado_juego["banderas_puestas"] += 1


            dibujar_juego(configuraciones.get_pantalla_pygame(), evento, estado_juego)

        pygame.display.flip()
        reloj.tick(30)

        

menu_interaccion()