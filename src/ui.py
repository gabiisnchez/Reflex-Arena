# ============================================
# ui.py - Funciones de interfaz de usuario
# ============================================

import pygame
from config import NEGRO, BLANCO, AMARILLO, GRIS_CLARO

# Dibuja texto en pantalla
def dibujar_texto(pantalla, texto, fuente, color, x, y, centro=False):

    # Renderizar el texto (convertirlo en imagen)
    superficie_texto = fuente.render (texto, True, color)

    # Si queremos centrar el texto
    if centro:
        rect = superficie_texto.get_rect(center=(x, y))
        pantalla.blit(superficie_texto, rect)
    else:
        # Si no, lo dibujamos desde la esquina superior izquierda
        pantalla.blit(superficie_texto, (x, y))

# Dibuja un botón interactivo que cambia al pasar el mouse
def dibujar_boton(pantalla, boton, texto, fuente, color_fondo, mouse_pos):

    # Verificar si el mouse está sobre el botón
    hover = boton.collidepoint(mouse_pos)

    if hover:
        # Si el mouse está encima, invertir colores
        pygame.draw.rect(pantalla, BLANCO, boton)
        dibujar_texto(pantalla ,texto, fuente, NEGRO, boton.centerx, boton.centery, True)
    else:
        # Si no está encime, colores normales
        pygame.draw.rect(pantalla, color_fondo, boton)
        pygame.draw.rect(pantalla, BLANCO, boton, 3)   # Borde blanco de 3px
        dibujar_texto(pantalla, texto, fuente, BLANCO, boton.centerx, boton.centery, True)

    return hover

# Dibuja una caja de texto donde el usuario puede escribir
def dibujar_input_box(pantalla, rect, texto, activo, fuente, max_chars=None):

    # El color cambia si la caja está activa
    color = AMARILLO if activo else GRIS_CLARO

    # Dibujar fondo negro
    pygame.draw.rect(pantalla, NEGRO, rect)

    # Dibujar borde (amarillo si activo, gris si no)
    pygame.draw.rect(pantalla, color, rect, 2)

    # Renderizar el texto escrito
    texto_surface =  fuente.render(texto, True, BLANCO)
    pantalla.blit(texto_surface, (rect.x + 10, rect.y + 10))

    # Mostrar cursor parpadeante si esta activo
    if activo and int(pygame.time.get_ticks() / 500) % 2:
        cursor_x = rect.x + 10 + texto_surface.get_width() + 2
        pygame.draw.line(pantalla, AMARILLO, (cursor_x, rect.y + 8), (cursor_x, rect.y + rect.height - 8), 2)