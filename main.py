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
    pygame.display.set_caption("⚡ REFLEJOS RÁPIDOS ⚡")
    
    # Crear diccionario de fuentes
    fuentes = {
        'grande': pygame.font.Font(None, 74),
        'mediana': pygame.font.Font(None, 48),
        'pequeña': pygame.font.Font(None, 36)
    }
    
    # Reloj para controlar FPS
    reloj = pygame.time.Clock()
    
    # Inicializar sistema de puntuaciones
    sistema_puntuaciones = SistemaPuntuaciones()

    # Inicializar sistema de sonidos
    gestor_sonidos = GestorSonidos()
    
    # Registro inicial del jugador
    pantalla_registro = PantallaRegistro(pantalla, fuentes)
    jugador = pantalla_registro.mostrar()
    
    # Si el usuario cerró la ventana, salir
    if jugador is None:
        pygame.quit()
        return
    
    # Bucle principal del juego
    while True:
        # Pantalla de inicio
        pantalla_inicio = PantallaInicio(pantalla, fuentes)
        iniciar = pantalla_inicio.mostrar()
        
        if iniciar is None:
            break
        
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
        
        # Pantalla final con ranking
        pantalla_final = PantallaFinal(
            pantalla, fuentes, jugador, 
            pantalla_juego.puntuacion, 
            pantalla_juego.clicks_fallados,
            sistema_puntuaciones,
            gestor_sonidos
        )
        
        if not pantalla_final.mostrar():
            break
    
    # Cerrar Pygame limpiamente
    pygame.quit()

if __name__ == "__main__":
    main()