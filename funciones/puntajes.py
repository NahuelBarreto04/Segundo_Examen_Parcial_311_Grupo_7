import pygame

def dibujar_victoria(pantalla):
    fuente = pygame.font.SysFont("arial", 60, bold=True)
    texto = fuente.render("GANASTE!", True, (0, 255, 0))
    sombra = fuente.render("GANASTE!", True, (0, 0, 0))

    x = (pantalla.get_width() - texto.get_width()) // 2
    y = pantalla.get_height() // 2 - texto.get_height() // 2

    fondo_rect = pygame.Rect(x - 20, y - 20, texto.get_width() + 40, texto.get_height() + 40)
    pygame.draw.rect(pantalla, (20, 20, 20), fondo_rect, border_radius=15)

    pantalla.blit(sombra, (x + 3, y + 3))
    pantalla.blit(texto, (x, y))
