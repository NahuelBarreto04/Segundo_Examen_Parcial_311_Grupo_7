import pygame
def suma():
    print("2+2")

#DIBUJAR BOTON
def dibujar_boton(pantalla, rect, color, texto, fuente, texto_color):
    #dibujar boton
    pygame.draw.rect(pantalla, color,rect, border_radius=10)

    #mostrar el texto
    texto = fuente.render(texto, True, texto_color)

    #Centrar el texto 
    pos_texto_x = rect.x + (rect.width // 2) - (texto.get_width() // 2)
    pos_texto_y = rect.y + (rect.height // 2) - (texto.get_height() // 2)
    
    #dibujar sobre la pantalla
    pantalla.blit(texto, (pos_texto_x,pos_texto_y))

