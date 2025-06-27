import pygame

dificultad_actual = "facil"
pantalla_actual = "menu"
BOTONES = []

def get_pantalla_actual():
    return pantalla_actual

def set_pantalla_actual(valor):
    global pantalla_actual
    pantalla_actual = valor

def get_dificultad_actual():
    return dificultad_actual

def set_dificultad_actual(valor):
    global dificultad_actual
    dificultad_actual = valor

def mostrar_textos(pantalla):
    fuente = pygame.font.SysFont("arial", pantalla.get_height() // 8)
    texto = fuente.render("BUSCAMINAS", True, (255, 255, 255))
    x = (pantalla.get_width() - texto.get_width()) // 2
    y = 30
    pantalla.blit(texto, (x, y))

def dibujar_botones(pantalla):
    BOTONES.clear()
    textos = ["Jugar", f"Dificultad: ({dificultad_actual})", "Puntajes", "Salir"]
    funciones = [jugar, cambiar_dificultad, ver_puntajes, salir]

    for i in range(len(textos)):
        w = pantalla.get_width() // 4
        h = pantalla.get_height() // 12
        x = (pantalla.get_width() - w) // 2
        y = pantalla.get_height() // 3 + i * (h + 20)

        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(pantalla, (100, 100, 100), rect)
    
        fuente = pygame.font.SysFont("arial", h // 2)
        texto = fuente.render(textos[i], True, (255, 255, 255))
        pantalla.blit(texto, (x + (w - texto.get_width()) // 2, y + (h - texto.get_height()) // 2))
        BOTONES.append((rect, funciones[i]))



def manejar_click(pos):
    for rect, funcion in BOTONES:
        print(rect.collidepoint(pos))
        if rect.collidepoint(pos):
            funcion()

def jugar():
    set_pantalla_actual("juego")

def cambiar_dificultad():
    global dificultad_actual
    if dificultad_actual == "facil":
        dificultad_actual = "normal"
    elif dificultad_actual == "normal":
        dificultad_actual = "dificil"
    else:
        dificultad_actual = "facil"

def ver_puntajes():
    print("PUNTAJES")

def salir():
    pygame.quit()
    exit()
