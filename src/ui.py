# ============================================
# ui.py - Funciones de interfaz de usuario
# ============================================

import pygame
from src.config import *

# Dibuja texto en pantalla con sombra opcional
def dibujar_texto(pantalla, texto, fuente, color, x, y, centro=False, sombra=False):
    if sombra:
        superficie_sombra = fuente.render(texto, True, NEGRO)
        if centro:
            rect_sombra = superficie_sombra.get_rect(center=(x + 2, y + 2))
            pantalla.blit(superficie_sombra, rect_sombra)
        else:
            pantalla.blit(superficie_sombra, (x + 2, y + 2))

    superficie_texto = fuente.render(texto, True, color)
    if centro:
        rect = superficie_texto.get_rect(center=(x, y))
        pantalla.blit(superficie_texto, rect)
    else:
        pantalla.blit(superficie_texto, (x, y))

def dibujar_panel(pantalla, x, y, ancho, alto, color=COLOR_PANEL, alpha=230, borde=True):
    """Dibuja un panel semi-transparente con bordes redondeados."""
    s = pygame.Surface((ancho, alto), pygame.SRCALPHA)
    pygame.draw.rect(s, (*color, alpha), s.get_rect(), border_radius=15)
    
    if borde:
        pygame.draw.rect(s, GRIS_CLARO, s.get_rect(), 2, border_radius=15)
        
    pantalla.blit(s, (x, y))

# Dibuja un botón interactivo moderno
def dibujar_boton(pantalla, boton, texto, fuente, color_fondo, mouse_pos):
    hover = boton.collidepoint(mouse_pos)
    
    # Colores dinámicos
    color_actual = list(color_fondo)
    if hover:
        # Hacer el color más brillante al pasar el mouse
        color_actual = [min(255, c + 30) for c in color_actual]
        # Efecto de elevación (sombra más grande)
        sombra = pygame.Rect(boton.x + 2, boton.y + 4, boton.width, boton.height)
        offset_y = -2
    else:
        sombra = pygame.Rect(boton.x + 4, boton.y + 6, boton.width, boton.height)
        offset_y = 0

    # Dibujar sombra
    pygame.draw.rect(pantalla, (0, 0, 0, 100), sombra, border_radius=12)
    
    # Botón principal
    rect_dibujo = pygame.Rect(boton.x, boton.y + offset_y, boton.width, boton.height)
    pygame.draw.rect(pantalla, color_actual, rect_dibujo, border_radius=12)
    
    # Borde brillante
    pygame.draw.rect(pantalla, (255, 255, 255, 50), rect_dibujo, 2, border_radius=12)

    # Texto con sombra sutil
    dibujar_texto(pantalla, texto, fuente, BLANCO, rect_dibujo.centerx, rect_dibujo.centery, True, sombra=True)

    return hover

# Dibuja una caja de texto moderna
def dibujar_input_box(pantalla, rect, texto, activo, fuente):
    # Fondo del input
    color_fondo = (20, 20, 30)
    pygame.draw.rect(pantalla, color_fondo, rect, border_radius=8)
    
    # Borde: Brillante si está activo
    color_borde = COLOR_RESALTE if activo else GRIS
    ancho_borde = 3 if activo else 1
    pygame.draw.rect(pantalla, color_borde, rect, ancho_borde, border_radius=8)
    
    if activo:
        # Glow externo sutil
        s = pygame.Surface((rect.width + 10, rect.height + 10), pygame.SRCALPHA)
        pygame.draw.rect(s, (*COLOR_RESALTE, 30), s.get_rect(), border_radius=12)
        pantalla.blit(s, (rect.x - 5, rect.y - 5))

    # Texto
    texto_surface = fuente.render(texto, True, BLANCO)
    pantalla.blit(texto_surface, (rect.x + 15, rect.y + 12))

    # Cursor
    if activo and int(pygame.time.get_ticks() / 500) % 2:
        cursor_x = rect.x + 15 + texto_surface.get_width() + 2
        pygame.draw.line(pantalla, COLOR_RESALTE, (cursor_x, rect.y + 10), (cursor_x, rect.y + rect.height - 10), 2)

# Clase para un menú desplegable moderno
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
        self.scroll_offset = 0
        self.max_visible_options = max_visible_options
        self.rect_menu = pygame.Rect(x, y + h + 5, w, h * min(len(options), max_visible_options))

    def dibujar(self, screen):
        # Fondo y borde del campo principal
        pygame.draw.rect(screen, (20, 20, 30), self.rect, border_radius=8)
        
        color_borde = COLOR_ACCENTO
        if self.rect.collidepoint(pygame.mouse.get_pos()) or self.is_open:
            color_borde = COLOR_RESALTE
            
        pygame.draw.rect(screen, color_borde, self.rect, 2, border_radius=8)
        
        # Texto seleccionado
        text = self.selected_option if self.selected_option else "Seleccionar Curso..."
        color_texto = BLANCO if self.selected_option else GRIS
        msg = self.font.render(text, 1, color_texto)
        screen.blit(msg, (self.rect.x + 15, self.rect.centery - msg.get_height()//2))

        # Dibujar lista desplegable
        if self.is_open:
            # Fondo del menú con sombra
            screen_rect = screen.get_rect()
            
            # Dibujar un fondo oscuro detrás del menú para resaltarlo
            s = pygame.Surface((self.rect_menu.width, self.rect_menu.height), pygame.SRCALPHA)
            pygame.draw.rect(s, (26, 26, 46, 250), s.get_rect(), border_radius=8)
            screen.blit(s, self.rect_menu.topleft)
            
            # Borde del menú
            pygame.draw.rect(screen, COLOR_ACCENTO, self.rect_menu, 2, border_radius=8)
            
            visible_options = self.options[self.scroll_offset : self.scroll_offset + self.max_visible_options]
            
            for i, option in enumerate(visible_options):
                rect_opcion = pygame.Rect(self.rect_menu.x, self.rect_menu.y + i * self.rect.height, self.rect.width, self.rect.height)
                
                # Highlight
                if rect_opcion.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen, COLOR_ACCENTO, rect_opcion, border_radius=4)
                
                msg = self.font.render(option, 1, BLANCO)
                screen.blit(msg, (rect_opcion.x + 15, rect_opcion.centery - msg.get_height()//2))
                
            # Scrollbar simple
            if len(self.options) > self.max_visible_options:
                scroll_h = self.rect_menu.height * (self.max_visible_options / len(self.options))
                scroll_y = self.rect_menu.y + (self.scroll_offset / len(self.options)) * self.rect_menu.height
                pygame.draw.rect(screen, GRIS, (self.rect_menu.right - 8, scroll_y, 4, scroll_h), border_radius=2)

    def manejar_evento(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.is_open = not self.is_open
                    return True
                elif self.is_open:
                    visible_options = self.options[self.scroll_offset : self.scroll_offset + self.max_visible_options]
                    for i, option in enumerate(visible_options):
                        rect = pygame.Rect(self.rect_menu.x, self.rect_menu.y + i * self.rect.height, self.rect.width, self.rect.height)
                        if rect.collidepoint(event.pos):
                            self.selected_option = option
                            self.is_open = False
                            return True
                    
                    if not self.rect_menu.collidepoint(event.pos):
                        self.is_open = False
                        
            elif event.button == 4 and self.is_open:
                self.scroll_offset = max(0, self.scroll_offset - 1)
                return True
            elif event.button == 5 and self.is_open:
                self.scroll_offset = min(len(self.options) - self.max_visible_options, self.scroll_offset + 1)
                return True
        return False

    def obtener_valor(self):
        return self.selected_option