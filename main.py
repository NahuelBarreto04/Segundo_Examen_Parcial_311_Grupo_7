import pygame
from funciones.pantallas import *
from funciones.menu import *
from funciones import *
from funciones.utilidad import IMAGENES, SONIDOS
from funciones.puntajes import *

pygame.init()
pygame.font.init()
pygame.display.set_caption("Buscaminas")
pygame.mixer.init()
COLOR_FONDO = (54, 54, 54)
ANCHO_INICIAL, ALTO_INICIAL = configuraciones.get_resolucion_actual()
PANTALLA = pygame.display.set_mode((ANCHO_INICIAL, ALTO_INICIAL), pygame.SCALED)
configuraciones.set_pantalla_pygame(PANTALLA)

estado_juego = {
    "juego_iniciado": False,
    "perdio": False,
    "musica_actual": None,
    "gano": False,
    "pedir_nombre": False,
    "nombre_jugador": "",
    "puntaje_mostrado": False
}






def pantalla_menu():
    """
    Muestra el menu principal.
    Carga la imagen de fondo, dibuja los textos y los botones,
    y actualiza la pantalla con todo eso.
    Usa funciones de otros archivos para cada parte.
    """
    pantalla = configuraciones.get_pantalla_pygame()
    imagen_fondo = pygame.transform.scale(IMAGENES["fondo"], (pantalla.get_width(), pantalla.get_height()))
    pantalla.blit(imagen_fondo, (0, 0))
    mostrar_textos(pantalla)
    dibujar_botones(pantalla)
    pygame.display.flip()



#FUNCION PRINCIPAL

def menu_interaccion():
    """
    bucle principal de el jugo
    
    -detecta eventos del mouse y del sistema
    -muestra las pantallas("menu","juego","puntajes")
    -reproduce la musica correspondiente
    -pidce el nombre del jugador en caso de victoria
    -en juego(permite hacer click para revelar celdas o  para colocar banderas)
    -verifica si el jugador gana o pierde
    """
    reloj = pygame.time.Clock()

    while True:
        evento = None
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                pygame.mixer.music.stop()
                return
            evento = e

        if estado_juego.get("pedir_nombre") == True:
            nombre = pedir_nombres(configuraciones.get_pantalla_pygame())
            estado_juego["nombre_jugador"] = nombre
            estado_juego["pedir_nombre"] = False
            guardar_puntaje(nombre, estado_juego["puntaje"])

        if configuraciones.get_pantalla_actual() == "menu":
            reproducir_musica("musica_menu", estado_juego)
            if evento and evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                manejar_click(evento.pos, estado_juego)
            pantalla_menu()

        elif configuraciones.get_pantalla_actual() == "puntaje":
            reproducir_musica("musica_puntajes", estado_juego)
            pantalla_puntajes(configuraciones.get_pantalla_pygame(), evento, estado_juego)

        elif configuraciones.get_pantalla_actual() == "juego":
            reproducir_musica("No", estado_juego)
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
                                generar_minas(estado_juego["tablero"], estado_juego["minas"], fila, col)
                                estado_juego["minas_generadas"] = True
                                calcular_numeros(estado_juego["tablero"])

                            if estado_juego["perdio"] == False:
                                resultado = revelar_celda(estado_juego, fila, col)
                                if resultado == "perdiste":
                                    estado_juego["perdio"] = True
                                    estado_juego["tiempo_final"] = (pygame.time.get_ticks() - estado_juego["inicio_timer"]) // 1000
                                    pygame.mixer.music.stop()
                                    reproducir_sonido("sonido_derrota")

                                else:
                                    if verificar_ganador(estado_juego):
                                        estado_juego["gano"] = True
                                        estado_juego["tiempo_final"] = (pygame.time.get_ticks() - estado_juego["inicio_timer"]) // 1000
                                        dificultad = configuraciones.get_dificultad_actual()
                                        pygame.mixer.music.stop()
                                        reproducir_sonido("sonido_victoria")
                                        tiempo = estado_juego["tiempo_final"]
                                        estado_juego["puntaje"] = calcular_puntaje(dificultad, tiempo)
                                        estado_juego["pedir_nombre"] = True
                                        
                        
                        
                        elif evento.button == 3:  # Click derecho
                            celda = estado_juego["tablero"][fila][col]
                            # si la celda no esta revelada
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

        

menu_interaccion()