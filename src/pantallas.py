# ============================================
# pantallas.py - Pantallas del juego
# ============================================

import pygame
from src.config import *
from src.circulo import Circulo
from src.ui import dibujar_texto, dibujar_boton, dibujar_input_box

# Pantalla donde el jugador introduce su nombre y curso
class PantallaRegistro:

    # Constructor de la pantalla de registro
    def __init__(self, pantalla, fuentes):

        self.pantalla = pantalla
        self.fuentes = fuentes
        self.nombre = ""
        self.curso = ""
        self.input_activo = "nombre"
        
        self.input_nombre = pygame.Rect(ANCHO//2 - 200, 250, 400, 50)
        self.input_curso = pygame.Rect(ANCHO//2 - 200, 350, 400, 50)
        self.boton_continuar = pygame.Rect(ANCHO//2 - 150, 470, 300, 50)
        

    # Muestra la pantalla de registro y gestiona la entrada de datos
    def mostrar(self):

        while True:
            self.pantalla.fill(NEGRO)
            
            dibujar_texto(self.pantalla, "REGISTRO DE JUGADOR", 
                            self.fuentes['grande'], AMARILLO, ANCHO//2, 100, True)
            
            dibujar_texto(self.pantalla, "Introduce tus datos para comenzar", 
                            self.fuentes['pequeña'], BLANCO, ANCHO//2, 170, True)
            
            dibujar_texto(self.pantalla, "Nombre:", 
                            self.fuentes['mediana'], BLANCO, ANCHO//2 - 200, 210)
            dibujar_texto(self.pantalla, "Curso (ej: 1º ESO, 2º BACH):", 
                            self.fuentes['mediana'], BLANCO, ANCHO//2 - 200, 310)
            
            dibujar_input_box(self.pantalla, self.input_nombre, self.nombre, 
                            self.input_activo == "nombre", self.fuentes['mediana'])
            dibujar_input_box(self.pantalla, self.input_curso, self.curso, 
                            self.input_activo == "curso", self.fuentes['mediana'])
            
            mouse_pos = pygame.mouse.get_pos()
            
            puede_continuar = len(self.nombre.strip()) > 0 and len(self.curso.strip()) > 0
            color_boton = VERDE if puede_continuar else GRIS
            
            if puede_continuar:
                dibujar_boton(self.pantalla, self.boton_continuar, "CONTINUAR", 
                            self.fuentes['mediana'], color_boton, mouse_pos)
            else:
                pygame.draw.rect(self.pantalla, color_boton, self.boton_continuar)
                pygame.draw.rect(self.pantalla, GRIS_CLARO, self.boton_continuar, 3)
                dibujar_texto(self.pantalla, "CONTINUAR", self.fuentes['mediana'], 
                            GRIS_CLARO, self.boton_continuar.centerx, 
                            self.boton_continuar.centery, True)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return None
                
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_nombre.collidepoint(evento.pos):
                        self.input_activo = "nombre"
                    elif self.input_curso.collidepoint(evento.pos):
                        self.input_activo = "curso"
                    elif self.boton_continuar.collidepoint(evento.pos) and puede_continuar:
                        return {"nombre": self.nombre.strip(), "curso": self.curso.strip()}
                
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_BACKSPACE:
                        if self.input_activo == "nombre":
                            self.nombre = self.nombre[:-1]
                        else:
                            self.curso = self.curso[:-1]
                    elif evento.key == pygame.K_TAB:
                        self.input_activo = "curso" if self.input_activo == "nombre" else "nombre"
                    elif evento.key == pygame.K_RETURN and puede_continuar:
                        return {"nombre": self.nombre.strip(), "curso": self.curso.strip()}
                    else:
                        if self.input_activo == "nombre" and len(self.nombre) < 20:
                            self.nombre += evento.unicode
                        elif self.input_activo == "curso" and len(self.curso) < 15:
                            self.curso += evento.unicode
            
            pygame.display.flip()


# Pantalla de inicio con información del juego y botón para empezar
class PantallaInicio:
    """"""
    
    def __init__(self, pantalla, fuentes):
        """Constructor de la pantalla de inicio."""
        self.pantalla = pantalla
        self.fuentes = fuentes
        
    def mostrar(self):
        """Muestra la pantalla de inicio."""
        while True:
            self.pantalla.fill(NEGRO)
            
            # Título con efecto de colores
            for i, letra in enumerate("REFLEJOS RÁPIDOS"):
                color = COLORES_TITULO[i % len(COLORES_TITULO)]
                texto = self.fuentes['grande'].render(letra, True, color)
                self.pantalla.blit(texto, (100 + i * 45, 80))
            
            dibujar_texto(self.pantalla, "¡Haz clic en los círculos lo más rápido posible!", 
                            self.fuentes['pequeña'], BLANCO, ANCHO//2, 200, True)
            dibujar_texto(self.pantalla, "Los círculos pequeños valen MÁS puntos", 
                            self.fuentes['pequeña'], AMARILLO, ANCHO//2, 240, True)
            
            dibujar_texto(self.pantalla, f"⏱️  {TIEMPO_JUEGO} SEGUNDOS DE PURA ADRENALINA", 
                            self.fuentes['mediana'], ROJO, ANCHO//2, 300, True)
            dibujar_texto(self.pantalla, f"🎯 {NUM_CIRCULOS} círculos simultáneos", 
                            self.fuentes['pequeña'], BLANCO, ANCHO//2, 350, True)
            dibujar_texto(self.pantalla, "⚡ Velocidad aumentada", 
                            self.fuentes['pequeña'], BLANCO, ANCHO//2, 390, True)
            
            boton_jugar = pygame.Rect(ANCHO//2 - 200, 460, 400, 70)
            mouse_pos = pygame.mouse.get_pos()
            
            dibujar_boton(self.pantalla, boton_jugar, "¡EMPEZAR DESAFÍO!", 
                        self.fuentes['grande'], VERDE, mouse_pos)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return None
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_jugar.collidepoint(evento.pos):
                        return True
            
            pygame.display.flip()


# Pantalla del juego donde se juega
class PantallaJuego:
    
    # Constructor de la pantalla de juego
    def __init__(self, pantalla, fuentes):

        self.pantalla = pantalla
        self.fuentes = fuentes
        self.circulos = [Circulo(ANCHO, ALTO) for _ in range(NUM_CIRCULOS)]
        self.puntuacion = 0
        self.clicks_fallados = 0
        self.tiempo_inicio = pygame.time.get_ticks()
        

    # Actualiza el tiempo del juego
    def actualizar(self):

        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = (tiempo_actual - self.tiempo_inicio) / 1000
        tiempo_restante = max(0, TIEMPO_JUEGO - tiempo_transcurrido)
        return tiempo_restante
    

    # Procesa un click del mouse
    def manejar_click(self, pos):

        click_x, click_y = pos
        circulo_clickeado = False
        
        for circulo in self.circulos[:]:
            if circulo.clicked(click_x, click_y):
                self.puntuacion += circulo.puntos
                self.circulos.remove(circulo)
                self.circulos.append(Circulo(ANCHO, ALTO))
                circulo_clickeado = True
                break
        
        if not circulo_clickeado:
            self.clicks_fallados += 1
            self.puntuacion = max(0, self.puntuacion - 1)
    

    # Mueve todos los círculos
    def mover_circulos(self):

        for circulo in self.circulos:
            circulo.mover()
    

    # Dibuja el estado actual del juego
    def dibujar(self, tiempo_restante):

        self.pantalla.fill(NEGRO)
        
        pygame.draw.rect(self.pantalla, AZUL, (0, 0, ANCHO, 100))
        pygame.draw.rect(self.pantalla, BLANCO, (0, 0, ANCHO, 100), 3)
        
        dibujar_texto(self.pantalla, f"PUNTOS: {self.puntuacion}", 
                        self.fuentes['mediana'], AMARILLO, 20, 30)
        
        color_tiempo = VERDE if tiempo_restante > 10 else (AMARILLO if tiempo_restante > 5 else ROJO)
        dibujar_texto(self.pantalla, f"TIEMPO: {int(tiempo_restante)}s", 
                        self.fuentes['mediana'], color_tiempo, ANCHO - 250, 30)
        
        for circulo in self.circulos:
            circulo.dibujar(self.pantalla, self.fuentes['pequeña'])


# Pantalla final con resultados y ranking
class PantallaFinal:

    # Constructor de la pantalla final    
    def __init__(self, pantalla, fuentes, jugador, puntuacion, clicks_fallados, sistema_puntuaciones):

        self.pantalla = pantalla
        self.fuentes = fuentes
        self.jugador = jugador
        self.puntuacion = puntuacion
        self.clicks_fallados = clicks_fallados
        self.sistema = sistema_puntuaciones
        
        self.sistema.agregar_puntuacion(
            jugador["nombre"], jugador["curso"], puntuacion, clicks_fallados
        )
        
        self.posicion = self.sistema.obtener_posicion(puntuacion)
        self.top10 = self.sistema.obtener_top10()
        
    # Muestra la pantalla final con resultados
    def mostrar(self):

        while True:
            self.pantalla.fill(NEGRO)
            
            dibujar_texto(self.pantalla, "¡JUEGO TERMINADO!", 
                            self.fuentes['grande'], AMARILLO, ANCHO//2, 40, True)
            
            dibujar_texto(self.pantalla, f"{self.jugador['nombre']} - {self.jugador['curso']}", 
                            self.fuentes['pequeña'], BLANCO, ANCHO//2, 100, True)
            
            dibujar_texto(self.pantalla, f"Puntuación: {self.puntuacion}", 
                            self.fuentes['mediana'], VERDE, ANCHO//2, 140, True)
            
            dibujar_texto(self.pantalla, f"Posición: #{self.posicion} de {self.sistema.obtener_total_jugadores()}", 
                            self.fuentes['mediana'], ROSA, ANCHO//2, 180, True)
            
            if self.posicion == 1:
                mensaje = "🏆 ¡NUEVO RÉCORD! ¡Eres el número 1! 🏆"
            elif self.posicion <= 3:
                mensaje = "🥇 ¡TOP 3! ¡Increíble! 🥇"
            elif self.posicion <= 10:
                mensaje = "⭐ ¡TOP 10! ¡Muy bien! ⭐"
            elif self.puntuacion > 80:
                mensaje = "💪 ¡Excelente puntuación! 💪"
            elif self.puntuacion > 50:
                mensaje = "👍 ¡Buen trabajo! ¡Sigue así! 👍"
            else:
                mensaje = "🎯 ¡Buen intento! ¡Puedes mejorar! 🎯"
            
            dibujar_texto(self.pantalla, mensaje, self.fuentes['pequeña'], 
                            AMARILLO, ANCHO//2, 220, True)
            
            dibujar_texto(self.pantalla, "═══ TOP 10 ═══", 
                            self.fuentes['mediana'], NARANJA, ANCHO//2, 260, True)
            
            y_pos = 300
            for i, record in enumerate(self.top10, 1):
                color = AMARILLO if i <= 3 else BLANCO
                
                medalla = ""
                if i == 1:
                    medalla = "🥇"
                elif i == 2:
                    medalla = "🥈"
                elif i == 3:
                    medalla = "🥉"
                
                texto = f"{medalla}{i}. {record['nombre'][:12]} ({record['curso']}) - {record['puntuacion']} pts"
                dibujar_texto(self.pantalla, texto, self.fuentes['pequeña'], 
                            color, ANCHO//2, y_pos, True)
                y_pos += 30
            
            boton_reintentar = pygame.Rect(50, 540, 300, 45)
            boton_salir = pygame.Rect(450, 540, 300, 45)
            
            mouse_pos = pygame.mouse.get_pos()
            
            dibujar_boton(self.pantalla, boton_reintentar, "JUGAR DE NUEVO", 
                            self.fuentes['pequeña'], VERDE, mouse_pos)
            dibujar_boton(self.pantalla, boton_salir, "SALIR", 
                            self.fuentes['pequeña'], ROJO, mouse_pos)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_reintentar.collidepoint(evento.pos):
                        return True
                    elif boton_salir.collidepoint(evento.pos):
                        return False
            
            pygame.display.flip()