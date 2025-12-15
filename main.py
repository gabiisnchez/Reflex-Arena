# ============================================
# main.py - Archivo principal
# ============================================

import pygame
from src.config import ANCHO, ALTO, FPS
from src.pantallas import PantallaRegistro, PantallaInicio, PantallaJuego, PantallaFinal
from src.puntuaciones import SistemaPuntuaciones
from src.sonidos import GestorSonidos

# Función principal que ejecuta el juego
def main():

    # Inicializar Pygame
    pygame.init()
    
    # Crear ventana
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Reflex-Arena")
    
    # Intentar cargar fuente de Emojis de Windows explícitamente
    # Primero buscamos el path
    font_path = pygame.font.match_font('segoeuiemoji')
    
    # Si no lo encuentra por nombre, intentamos una ruta común (Windows)
    if not font_path:
         import os
         possible_path = r"C:\Windows\Fonts\seguiemj.ttf"
         if os.path.exists(possible_path):
             font_path = possible_path

    print(f"DEBUG: Fuente emoji encontrada en: {font_path}")

    # Definir función helper para cargar
    def cargar_fuente(size):
        if font_path:
            try:
                f = pygame.font.Font(font_path, size)
                return f
            except Exception as e:
                print(f"DEBUG: Error cargando fuente {font_path}: {e}")
        # Fallback
        print("DEBUG: Usando Arial como fallback")
        return pygame.font.SysFont("arial", size)

    fuentes = {
        'grande': pygame.font.Font(None, 48),
        'mediana': pygame.font.Font(None, 32),
        'pequeña': pygame.font.Font(None, 24),
        'emoji_pequeña': cargar_fuente(24)
    }
    
    # Reloj para controlar FPS
    reloj = pygame.time.Clock()
    
    # Inicializar sistema de puntuaciones
    sistema_puntuaciones = SistemaPuntuaciones()

    # Inicializar sistema de sonidos
    gestor_sonidos = GestorSonidos()
    
    # Bucle de sesión (cambio de usuario)
    while True:
        # Registro del jugador
        pantalla_registro = PantallaRegistro(pantalla, fuentes)
        jugador = pantalla_registro.mostrar()
        
        # Si el usuario cerró la ventana en el registro, salir
        if jugador is None:
            break
        
        # Bucle de juego (mismo usuario)
        while True:
            # Pantalla de inicio
            pantalla_inicio = PantallaInicio(pantalla, fuentes)
            iniciar = pantalla_inicio.mostrar()
            
            if iniciar is None:
                return # Salir de todo si cierran en inicio
            
            # Juego
            pantalla_juego = PantallaJuego(pantalla, fuentes, gestor_sonidos)
            ejecutando = True
            
            while ejecutando:
                reloj.tick(FPS)
                
                tiempo_restante = pantalla_juego.actualizar()
                
                if tiempo_restante <= 0:
                    ejecutando = False
                    continue
                
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        pantalla_juego.manejar_click(evento.pos)
                
                pantalla_juego.mover_circulos()
                pantalla_juego.dibujar(tiempo_restante)
                pygame.display.flip()
            
            # Detener sonido de tictac al terminar
            gestor_sonidos.detener_sonido("tictac")

            # Pantalla final con ranking
            pantalla_final = PantallaFinal(
                pantalla, fuentes, jugador, 
                pantalla_juego.puntuacion, 
                pantalla_juego.clicks_fallados,
                sistema_puntuaciones,
                gestor_sonidos
            )
            
            accion = pantalla_final.mostrar()
            
            if accion == "new_user":
                break # Sale del bucle de juego, vuelve al registro
            elif accion == "replay":
                continue # Vuelve al inicio del bucle de juego (PantallaInicio)
            elif accion is None:
                return # Cierra la aplicación
    
    # Cerrar Pygame limpiamente
    pygame.quit()

if __name__ == "__main__":
    main()