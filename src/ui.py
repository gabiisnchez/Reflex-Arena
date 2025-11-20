# ============================================
# ui.py - Funciones de interfaz de usuario
# ============================================

import pygame
from src.config import NEGRO, BLANCO, AMARILLO, GRIS_CLARO


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


# Clase para un menú desplegable
class Dropdown:
    def __init__(self, x, y, w, h, font, main_color, hover_color, text_color, options, max_visible_options=5):
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.main_color = main_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.options = options
        self.selected_option = None
        self.is_open = False
        self.active_option = -1
        
        # Scroll variables
        self.max_visible_options = max_visible_options
        self.scroll_offset = 0
        self.rect_menu = pygame.Rect(x, y + h, w, h * min(len(options), max_visible_options))

    def dibujar(self, screen):
        # Dibujar la caja principal
        color = self.hover_color if self.rect.collidepoint(pygame.mouse.get_pos()) else self.main_color
        pygame.draw.rect(screen, color, self.rect, 2)
        pygame.draw.rect(screen, NEGRO, self.rect.inflate(-4, -4))
        
        # Texto seleccionado o placeholder
        text = self.selected_option if self.selected_option else ""
        msg = self.font.render(text, 1, self.text_color)
        screen.blit(msg, msg.get_rect(center=self.rect.center))

        # Dibujar opciones si está abierto
        if self.is_open:
            # Dibujar fondo del menú
            pygame.draw.rect(screen, NEGRO, self.rect_menu)
            pygame.draw.rect(screen, self.main_color, self.rect_menu, 2)
            
            # Calcular opciones visibles
            visible_options = self.options[self.scroll_offset : self.scroll_offset + self.max_visible_options]
            
            for i, option in enumerate(visible_options):
                rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                
                # Highlight si el mouse está encima
                if rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen, self.hover_color, rect)
                
                # Dibujar texto
                msg = self.font.render(option, 1, self.text_color)
                screen.blit(msg, msg.get_rect(center=rect.center))
                
            # Dibujar barra de scroll si es necesario
            if len(self.options) > self.max_visible_options:
                scroll_h = self.rect_menu.height * (self.max_visible_options / len(self.options))
                scroll_y = self.rect_menu.y + (self.scroll_offset / len(self.options)) * self.rect_menu.height
                scroll_rect = pygame.Rect(self.rect.right - 10, scroll_y, 8, scroll_h)
                pygame.draw.rect(screen, GRIS_CLARO, scroll_rect)

    def manejar_evento(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Click izquierdo
                if self.rect.collidepoint(event.pos):
                    self.is_open = not self.is_open
                elif self.is_open:
                    # Verificar click en opciones visibles
                    visible_options = self.options[self.scroll_offset : self.scroll_offset + self.max_visible_options]
                    for i, option in enumerate(visible_options):
                        rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                        if rect.collidepoint(event.pos):
                            self.selected_option = option
                            self.is_open = False
                            return True
                    
                    # Si click fuera del menú, cerrar
                    if not self.rect_menu.collidepoint(event.pos):
                        self.is_open = False
                        
            elif event.button == 4 and self.is_open: # Scroll arriba
                self.scroll_offset = max(0, self.scroll_offset - 1)
            elif event.button == 5 and self.is_open: # Scroll abajo
                self.scroll_offset = min(len(self.options) - self.max_visible_options, self.scroll_offset + 1)
                
        return False

    def obtener_valor(self):
        return self.selected_option