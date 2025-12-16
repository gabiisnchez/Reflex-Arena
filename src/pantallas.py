# ============================================
# pantallas.py - Pantallas del juego
# ============================================

import pygame
import math
from src.config import *
from src.circulo import Circulo
from src.ui import dibujar_texto, dibujar_boton, dibujar_input_box, Dropdown, dibujar_panel

# Pantalla donde el jugador introduce su nombre y curso
class PantallaRegistro:

    # Constructor de la pantalla de registro
    def __init__(self, pantalla, fuentes):
        self.pantalla = pantalla
        self.fuentes = fuentes
        self.nombre = ""
        self.input_activo = "nombre"

        # Centrar panel
        panel_w = 400
        panel_h = 450
        self.panel_x = ANCHO//2 - panel_w//2
        self.panel_y = ALTO//2 - panel_h//2

        self.input_nombre = pygame.Rect(self.panel_x + 30, self.panel_y + 110, 340, 40)
        self.boton_continuar = pygame.Rect(ANCHO//2 - 120, self.panel_y + 360, 240, 50)

        opciones_curso = [
            "1º Acondicionamiento Físico", "2º Acondicionamiento Físico",
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
            "1º Integración Social", "2º Integración Social"
        ]

        self.dropdown_curso = Dropdown(
            self.panel_x + 30, self.panel_y + 200, 340, 40,
            fuentes['pequeña'],
            COLOR_PANEL,
            COLOR_ACCENTO,
            BLANCO,
            opciones_curso,
            max_visible_options=3
        )

    # Muestra la pantalla de registro y gestiona la entrada de datos
    def mostrar(self):
        clock = pygame.time.Clock()
        while True:
            self.pantalla.fill(COLOR_FONDO)

            # Dibujar un fondo sutil o patrón (opcional)
            for i in range(0, ANCHO, 40):
                pygame.draw.line(self.pantalla, (30, 30, 50), (i, 0), (i, ALTO), 1)
            for i in range(0, ALTO, 40):
                pygame.draw.line(self.pantalla, (30, 30, 50), (0, i), (ANCHO, i), 1)

            # Dibujar Panel
            dibujar_panel(self.pantalla, self.panel_x, self.panel_y, 400, 450)

            dibujar_texto(self.pantalla, "REGISTRO",
                            self.fuentes['grande'], AMARILLO, ANCHO//2, self.panel_y + 30, True, sombra=True)

            dibujar_texto(self.pantalla, "Nombre:",
                            self.fuentes['mediana'], BLANCO, self.panel_x + 30, self.panel_y + 80)
            
            dibujar_texto(self.pantalla, "Curso:",
                            self.fuentes['mediana'], BLANCO, self.panel_x + 30, self.panel_y + 170)

            dibujar_input_box(self.pantalla, self.input_nombre, self.nombre,
                            self.input_activo == "nombre", self.fuentes['pequeña'])

            # Dibujar Dropdown
            self.dropdown_curso.dibujar(self.pantalla)

            mouse_pos = pygame.mouse.get_pos()

            curso_seleccionado = self.dropdown_curso.obtener_valor()
            puede_continuar = len(self.nombre.strip()) > 0 and curso_seleccionado is not None
            
            # Botón Continuar
            color_btn = COLOR_RESALTE if puede_continuar else GRIS
            if puede_continuar:
                dibujar_boton(self.pantalla, self.boton_continuar, "INICIAR MISIÓN",
                            self.fuentes['pequeña'], color_btn, mouse_pos)
            else:
                 # Dibujar botón deshabilitado
                pygame.draw.rect(self.pantalla, list(color_btn) + [100], self.boton_continuar, border_radius=12)
                dibujar_texto(self.pantalla, "INICIAR MISIÓN", self.fuentes['pequeña'],
                            GRIS_CLARO, self.boton_continuar.centerx,
                            self.boton_continuar.centery, True)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return None

                # Manejar eventos del dropdown
                if self.dropdown_curso.manejar_evento(evento):
                    pass

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_nombre.collidepoint(evento.pos):
                        self.input_activo = "nombre"
                    elif self.boton_continuar.collidepoint(evento.pos) and puede_continuar:
                        return {"nombre": self.nombre.strip(), "curso": curso_seleccionado}
                    else:
                        self.input_activo = None

                elif evento.type == pygame.KEYDOWN:
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
            clock.tick(60)


# Pantalla de inicio con información del juego y botón para empezar
class PantallaInicio:

    def __init__(self, pantalla, fuentes):
        """Constructor de la pantalla de inicio."""
        self.pantalla = pantalla
        self.fuentes = fuentes
        self.start_ticks = pygame.time.get_ticks()

    def mostrar(self):
        """Muestra la pantalla de inicio."""
        clock = pygame.time.Clock()
        while True:
            self.pantalla.fill(COLOR_FONDO)
            
            # Efecto de fondo (lineas moviéndose)
            tiempo = pygame.time.get_ticks() / 1000
            for i in range(10):
                y = (tiempo * 50 + i * 60) % ALTO
                pygame.draw.line(self.pantalla, (30, 30, 50), (0, y), (ANCHO, y), 1)

            # Título con animación de pulso
            scale = 1.0 + 0.05 * math.sin(tiempo * 2)
            titulo_font = self.fuentes['grande']
            
            # Título principal
            txt_reflejos = "REFLEJOS RÁPIDOS"
            ancho_ref = titulo_font.size(txt_reflejos)[0]
            espacio = 20
            total_ancho = ancho_ref + espacio
            
            start_x = (ANCHO - total_ancho) // 2
            
            dibujar_texto(self.pantalla, txt_reflejos,
                            titulo_font, CIAN, start_x, 150, False, sombra=True)

            # Panel de instrucciones
            dibujar_panel(self.pantalla, ANCHO//2 - 350, 220, 700, 150)

            dibujar_texto(self.pantalla, "OBJETIVO DE LA MISIÓN:",
                            self.fuentes['mediana'], AMARILLO, ANCHO//2, 250, True)

            dibujar_texto(self.pantalla, "1. Destruye los círculos haciendo clic.",
                            self.fuentes['pequeña'], BLANCO, ANCHO//2 - 300, 290, False)
            dibujar_texto(self.pantalla, "2. Los objetivos pequeños otorgan MÁS puntos.",
                            self.fuentes['pequeña'], ORANGE_RED if 'ORANGE_RED' in globals() else ROJO, ANCHO//2 - 300, 320, False)

            boton_jugar = pygame.Rect(ANCHO//2 - 150, 450, 300, 60)
            mouse_pos = pygame.mouse.get_pos()

            dibujar_boton(self.pantalla, boton_jugar, "INICIAR SISTEMA",
                        self.fuentes['mediana'], COLOR_RESALTE, mouse_pos)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return None
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_jugar.collidepoint(evento.pos):
                        return True

            pygame.display.flip()
            clock.tick(60)


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

        # Inicializar sistema de partículas
        from src.particulas import SistemaParticulas
        self.sistema_particulas = SistemaParticulas()

    # Actualiza el tiempo del juego
    def actualizar(self):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = (tiempo_actual - self.tiempo_inicio) / 1000
        tiempo_restante = max(0, TIEMPO_JUEGO - tiempo_transcurrido)

        if tiempo_restante <= 5 and tiempo_restante > 0 and not self.tictac_sonando:
            self.gestor_sonidos.reproducir_sonido("tictac")
            self.tictac_sonando = True

        # Actualizar partículas
        self.sistema_particulas.actualizar()

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

                # Lanzar explosión de partículas
                self.sistema_particulas.lanzar_explosion(click_x, click_y, circulo.color)

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
        for circulo in self.circulos[:]:
            circulo.mover()
            # Si el círculo expira (solo dorados por ahora), lo eliminamos y creamos uno nuevo
            if circulo.ha_expirado():
                self.circulos.remove(circulo)
                self.circulos.append(Circulo(ANCHO, ALTO))

    # Dibuja el estado actual del juego
    def dibujar(self, tiempo_restante):
        self.pantalla.fill(COLOR_FONDO)
        
        # UI HUD (Heads Up Display)
        dibujar_panel(self.pantalla, 0, 0, ANCHO, 80, color=COLOR_PANEL, alpha=240, borde=False)
        pygame.draw.line(self.pantalla, COLOR_ACCENTO, (0, 80), (ANCHO, 80), 2)

        # Puntuación
        dibujar_texto(self.pantalla, f"PUNTOS", self.fuentes['pequeña'], GRIS_CLARO, 100, 20, True)
        dibujar_texto(self.pantalla, f"{self.puntuacion}", self.fuentes['grande'], AMARILLO, 100, 50, True)

        # Combo
        if self.racha > 1:
            color_racha = BLANCO
            if self.racha >= 10:
                color_racha = ROJO
            elif self.racha >= 5:
                color_racha = AMARILLO

            dibujar_texto(self.pantalla, f"COMBO", self.fuentes['pequeña'], GRIS_CLARO, ANCHO//2, 20, True)
            dibujar_texto(self.pantalla, f"x{self.racha}", self.fuentes['grande'], color_racha, ANCHO//2, 50, True)
            
            # Barra de progreso del combo (visual)
            bar_width = min(200, self.racha * 20)
            pygame.draw.rect(self.pantalla, color_racha, (ANCHO//2 - bar_width//2, 70, bar_width, 4))

        # Tiempo
        # Tiempo
        color_tiempo = CIAN
        if tiempo_restante <= 10:
            color_tiempo = AMARILLO
        if tiempo_restante <= 5:
            color_tiempo = ROJO
            # Parpadeo crítico
            if int(tiempo_restante * 5) % 2 == 0:
                color_tiempo = BLANCO

        dibujar_texto(self.pantalla, f"TIEMPO", self.fuentes['pequeña'], GRIS_CLARO, ANCHO - 100, 20, True)
        dibujar_texto(self.pantalla, f"{int(tiempo_restante)}", self.fuentes['grande'], color_tiempo, ANCHO - 100, 50, True)

        # Area de juego
        # Dibujo de círculos
        for circulo in self.circulos:
            circulo.dibujar(self.pantalla, self.fuentes['pequeña'])

        # Dibujar partículas (encima de los círculos)
        self.sistema_particulas.dibujar(self.pantalla)


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
        clock = pygame.time.Clock()
        while True:
            self.pantalla.fill(COLOR_FONDO)

            dibujar_texto(self.pantalla, "MISIÓN FINALIZADA",
                            self.fuentes['grande'], AMARILLO, ANCHO//2, 30, True, sombra=True)

            # Panel de Resultado Personal
            dibujar_panel(self.pantalla, 50, 70, ANCHO - 100, 130)
            
            # Nombre y Curso centrados arriba
            dibujar_texto(self.pantalla, f"AGENTE: {self.jugador['nombre']}",
                            self.fuentes['mediana'], BLANCO, ANCHO//2, 85, True)
            dibujar_texto(self.pantalla, f"UNIDAD: {self.jugador['curso']}",
                            self.fuentes['pequeña'], GRIS_CLARO, ANCHO//2, 110, True)
            
            # Puntuación y Posición centrados debajo
            # Puntuación a la izquierda del centro
            dibujar_texto(self.pantalla, "PUNTUACIÓN", self.fuentes['pequeña'], CIAN, ANCHO//2 - 120, 135, True)
            dibujar_texto(self.pantalla, str(self.puntuacion), self.fuentes['grande'], VERDE, ANCHO//2 - 120, 160, True)
            
            # Posición a la derecha del centro
            dibujar_texto(self.pantalla, "POSICIÓN", self.fuentes['pequeña'], CIAN, ANCHO//2 + 120, 135, True)
            dibujar_texto(self.pantalla, f"#{self.posicion}", self.fuentes['grande'], MAGENTA, ANCHO//2 + 120, 160, True)

            # Mensaje de estado
            if self.posicion == 1:
                mensaje = "¡NUEVO RÉCORD ABSOLUTO!"
                color_msg = AMARILLO
            elif self.posicion <= 10:
                mensaje = "ESTÁS EN EL TOP 10"
                color_msg = CIAN
            else:
                mensaje = "BUEN INTENTO. SIGUE ENTRENANDO."
                color_msg = GRIS_CLARO

            dibujar_texto(self.pantalla, mensaje, self.fuentes['mediana'], color_msg, ANCHO//2, 215, True)

            # Tabla TOP 10
            dibujar_panel(self.pantalla, 80, 240, ANCHO - 160, 260)
            
            y_pos = 260
            for i, record in enumerate(self.top10, 1):
                color = BLANCO
                if i == 1: color = AMARILLO
                elif i == 2: color = GRIS_CLARO
                elif i == 3: color = ORANGE_RED if 'ORANGE_RED' in globals() else NARANJA

                bg_color = (255, 255, 255, 20) if i % 2 == 0 else (0, 0, 0, 0)
                if bg_color[3] > 0:
                     # Ajustar el ancho de la fila de fondo
                     s = pygame.Surface((ANCHO - 200, 22), pygame.SRCALPHA)
                     pygame.draw.rect(s, bg_color, s.get_rect(), border_radius=5)
                     self.pantalla.blit(s, (100, y_pos - 5))

                dibujar_texto(self.pantalla, f"#{i}", self.fuentes['pequeña'], color, 120, y_pos)
                # Mostrar más caracteres del nombre
                dibujar_texto(self.pantalla, f"{record['nombre'][:25]}", self.fuentes['pequeña'], color, 200, y_pos)
                dibujar_texto(self.pantalla, f"{record['puntuacion']}", self.fuentes['pequeña'], VERDE, ANCHO - 200, y_pos)

                
                y_pos += 25

            boton_reintentar = pygame.Rect(100, 530, 280, 50)
            boton_nuevo_juego = pygame.Rect(420, 530, 280, 50)
            mouse_pos = pygame.mouse.get_pos()

            dibujar_boton(self.pantalla, boton_reintentar, "REINTENTAR MISIÓN",
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
            clock.tick(60)

