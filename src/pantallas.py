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
        self.input_activo = "nombre"
        
        self.input_nombre = pygame.Rect(ANCHO//2 - 200, 250, 400, 50)
        self.boton_continuar = pygame.Rect(ANCHO//2 - 150, 470, 300, 50)
        
        # Inicializar Dropdown
        from src.ui import Dropdown
        opciones_curso = ["1º Acondicionamiento Físico","2º Acondicionamiento Físico", 
                            "1º TSEAS", "2º TSEAS", 
                            "1º TECO", "2º TECO", 
                            "1º DAM", "2º DAM", 
                            "1º DAW", "2º DAW", 
                            "1º SMR", "2º SMR",
                            "1º Anatomía Patológica", "2º Anatomía Patológica",
                            "1º Enfermería", "2º Enfermería",
                            "1º Dietética", "2º Dietética",
                            "1º Farmacia", "2º Farmacia",
                            "1º Higiene", "2º Higiene",
                            "1º Imagen", "2º Imagen",
                            "1º Laboratorio", "2º Laboratorio",
                            "1º Prótesis", "2º Prótesis",
                            "1º Atención a personas", "2º Atención a personas", 
                            "1º Infantil", "2º Infantil",
                            "1º Integración Social", "2º Integración Social"]
        self.dropdown_curso = Dropdown(
            ANCHO//2 - 200, 350, 400, 50, 
            fuentes['mediana'], 
            GRIS_CLARO, 
            AMARILLO, 
            BLANCO, 
            opciones_curso
        )
        

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
            dibujar_texto(self.pantalla, "Curso:", 
                            self.fuentes['mediana'], BLANCO, ANCHO//2 - 200, 310)
            
            dibujar_input_box(self.pantalla, self.input_nombre, self.nombre, 
                            self.input_activo == "nombre", self.fuentes['mediana'])
            
            # Dibujar Dropdown
            self.dropdown_curso.dibujar(self.pantalla)
            
            mouse_pos = pygame.mouse.get_pos()
            
            curso_seleccionado = self.dropdown_curso.obtener_valor()
            puede_continuar = len(self.nombre.strip()) > 0 and curso_seleccionado is not None
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
                
                # Manejar eventos del dropdown
                if self.dropdown_curso.manejar_evento(evento):
                    pass # El dropdown manejó el evento
                
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_nombre.collidepoint(evento.pos):
                        self.input_activo = "nombre"
                    elif self.boton_continuar.collidepoint(evento.pos) and puede_continuar:
                        return {"nombre": self.nombre.strip(), "curso": curso_seleccionado}
                
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_BACKSPACE:
                        if self.input_activo == "nombre":
                            self.nombre = self.nombre[:-1]
                    elif evento.key == pygame.K_TAB:
                        self.input_activo = "nombre"
                    elif evento.key == pygame.K_RETURN and puede_continuar:
                        return {"nombre": self.nombre.strip(), "curso": curso_seleccionado}
                    else:
                        if self.input_activo == "nombre" and len(self.nombre) < 20:
                            self.nombre += evento.unicode
            
            pygame.display.flip()


# Pantalla de inicio con información del juego y botón para empezar
class PantallaInicio:
    
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
    def __init__(self, pantalla, fuentes, gestor_sonidos):

        self.pantalla = pantalla
        self.fuentes = fuentes
        self.gestor_sonidos = gestor_sonidos
        self.circulos = [Circulo(ANCHO, ALTO) for _ in range(NUM_CIRCULOS)]
        self.puntuacion = 0
        self.clicks_fallados = 0
        self.racha = 0
        self.tiempo_inicio = pygame.time.get_ticks()
        self.tictac_sonando = False
        

    # Actualiza el tiempo del juego
    def actualizar(self):

        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = (tiempo_actual - self.tiempo_inicio) / 1000
        tiempo_restante = max(0, TIEMPO_JUEGO - tiempo_transcurrido)

        if tiempo_restante <= 5 and tiempo_restante > 0 and not self.tictac_sonando:
            self.gestor_sonidos.reproducir_sonido("tictac")
            self.tictac_sonando = True
        
        return tiempo_restante
    

    # Procesa un click del mouse
    def manejar_click(self, pos):

        click_x, click_y = pos
        circulo_clickeado = False
        
        for circulo in self.circulos[:]:
            if circulo.clicked(click_x, click_y):
                self.racha += 1
                bonus = 0
                if self.racha >= 10:
                    bonus = 2
                elif self.racha >= 5:
                    bonus = 1
                
                if self.racha == 5 or self.racha == 10:
                    self.gestor_sonidos.reproducir_sonido("bonus")
                
                self.puntuacion += circulo.puntos + bonus
                self.circulos.remove(circulo)
                self.circulos.append(Circulo(ANCHO, ALTO))
                circulo_clickeado = True
                self.gestor_sonidos.reproducir_sonido("click")
                break
        
        if not circulo_clickeado:
            self.racha = 0
            self.clicks_fallados += 1
            self.puntuacion = max(0, self.puntuacion - 1)
            self.gestor_sonidos.reproducir_sonido("fail")
    

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

        if self.racha > 1:
            color_racha = BLANCO
            if self.racha >= 10:
                color_racha = ROJO
            elif self.racha >= 5:
                color_racha = AMARILLO
            
            dibujar_texto(self.pantalla, f"COMBO x{self.racha}", 
                            self.fuentes['mediana'], color_racha, 20, 70)
        
        color_tiempo = VERDE if tiempo_restante > 10 else (AMARILLO if tiempo_restante > 5 else ROJO)
        dibujar_texto(self.pantalla, f"TIEMPO: {int(tiempo_restante)}s", 
                        self.fuentes['mediana'], color_tiempo, ANCHO - 250, 30)
        
        for circulo in self.circulos:
            circulo.dibujar(self.pantalla, self.fuentes['pequeña'])


# Pantalla final con resultados y ranking
class PantallaFinal:

    # Constructor de la pantalla final    
    def __init__(self, pantalla, fuentes, jugador, puntuacion, clicks_fallados, sistema_puntuaciones, gestor_sonidos):

        self.pantalla = pantalla
        self.fuentes = fuentes
        self.jugador = jugador
        self.puntuacion = puntuacion
        self.clicks_fallados = clicks_fallados
        self.sistema = sistema_puntuaciones
        self.gestor_sonidos = gestor_sonidos
        
        self.sistema.agregar_puntuacion(
            jugador["nombre"], jugador["curso"], puntuacion, clicks_fallados
        )
        
        self.posicion = self.sistema.obtener_posicion(puntuacion)
        self.top10 = self.sistema.obtener_top10()

        if self.posicion == 1:
            self.gestor_sonidos.reproducir_sonido("record")
        
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
            boton_nuevo_juego = pygame.Rect(450, 540, 300, 45)
            
            mouse_pos = pygame.mouse.get_pos()
            
            dibujar_boton(self.pantalla, boton_reintentar, "JUGAR DE NUEVO", 
                            self.fuentes['pequeña'], VERDE, mouse_pos)
            dibujar_boton(self.pantalla, boton_nuevo_juego, "NUEVO JUEGO", 
                            self.fuentes['pequeña'], AZUL, mouse_pos)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return None
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_reintentar.collidepoint(evento.pos):
                        return "replay"
                    elif boton_nuevo_juego.collidepoint(evento.pos):
                        return "new_user"
            
            pygame.display.flip()