# ============================================
# circulo.py - Clase Circulo
# ============================================

import random       # Para generar número aleatorios
import math         # Para operaciones matemáticas
import pygame
from src.config import COLORES_CIRCULOS, BLANCO, VELOCIDAD_MIN, VELOCIDAD_MAX, ORO, PROBABILIDAD_ORO

class Circulo:
    """
    Representa un círculo en el juego.
    
    Cada círculo tiene posición, tamaño, color, velocidad y valor en puntos.
    Se mueve rebotando en los bordes y puede detectar si fue clickeado.
    """


    # Constructor que inicializar un círculo con valores aleatorios
    def __init__(self, ancho, alto):

        # Guardar dimensiones de la pantalla
        self.ancho = ancho
        self.alto = alto

        # Radio aleatorio entre 20 y 50 píxeles
        self.radio = random.randint(20, 50)

        # Posición X aleatoria (pero sin salirse de la pantalla)
        self.x = random.randint(self.radio, ancho - self.radio)

        # Posición Y aleatorio (empezando desde y=80 para dejar espacio arriba para el HUD)
        self.y = random.randint(80 + self.radio, alto - self.radio)

        # Determinar si es un círculo dorado
        self.es_dorado = random.random() < PROBABILIDAD_ORO

        if self.es_dorado:
            self.color = ORO
            self.radio = random.randint(15, 25) # Más pequeño
            
            # Velocidad alta (5 a 8)
            velocidades = [i for i in range(5, 9)] + [i for i in range(-8, -4)]
            self.velocidad_x = random.choice(velocidades)
            self.velocidad_y = random.choice(velocidades)
            
            # Calcular puntos: Base 5 + Bonus por velocidad + Bonus por tamaño
            velocidad_abs = abs(self.velocidad_x)
            puntos_velocidad = 0
            if velocidad_abs >= 7: puntos_velocidad = 3
            elif velocidad_abs >= 5: puntos_velocidad = 1
            
            puntos_tamano = 0
            if self.radio <= 18: puntos_tamano = 2
            elif self.radio <= 22: puntos_tamano = 1
            
            self.puntos = 5 + puntos_velocidad + puntos_tamano
            self.duracion = random.randint(2000, 3000) # Duración de 2 a 3 segundos
            
        else:
            self.color = random.choice(COLORES_CIRCULOS)
            self.radio = random.randint(20, 50)
            self.duracion = None # No expira
            
            # Velocidades normales
            velocidades = [i for i in range(VELOCIDAD_MIN, VELOCIDAD_MAX + 1) if i != 0]
            self.velocidad_x = random.choice(velocidades)
            self.velocidad_y = random.choice(velocidades)

            # Calcular puntos según tamaño (más pequeño = más puntos)
            self.puntos = max(1, 6 - (self.radio // 10))
            
        self.tiempo_creacion = pygame.time.get_ticks()


    # Mueve el círculo según su velocidad y lo hace rebotar en los bordes
    def mover(self):

        # Actualizar posición
        self.x += self.velocidad_x
        self.y += self.velocidad_y

        # Rebotar en bordes horizontales
        if self.x - self.radio <= 0 or self.x + self.radio >= self.ancho:
            self.velocidad_x *= -1 # Invertir dirección X

        # Rebotar en bordes verticales (Límite superior = 80 para el HUD)
        if self.y - self.radio <= 80 or self.y + self.radio >= self.alto:
            self.velocidad_y *= -1 # Invertir dirección Y


    # Verifica si el círculo ha expirado (solo para círculos con duración limitada)
    def ha_expirado(self):
        if self.duracion is None:
            return False
        return pygame.time.get_ticks() - self.tiempo_creacion > self.duracion


    # Dibuja el círculo en la pantalla con su número de puntos
    def dibujar(self, superficie, fuente):

        if self.es_dorado:
            # Efecto de halo brillante para los dorados
            halo_radio = self.radio + 4
            tiempo = pygame.time.get_ticks()
            # Pulsación leve
            if (tiempo // 200) % 2 == 0:
                halo_radio += 2
            pygame.draw.circle(superficie, (255, 255, 200), (int(self.x), int(self.y)), halo_radio, 2)

        # Dibujar círculo relleno - NOTA: el centro debe ser una tupla (x, y)
        pygame.draw.circle(superficie, self.color, (int(self.x), int(self.y)), self.radio)
    
        # Dibujar borde blanco
        pygame.draw.circle(superficie, BLANCO, (int(self.x), int(self.y)), self.radio, 3)
        
        # Dibujar número de puntos en el centro
        color_texto = BLANCO
        if self.es_dorado:
            color_texto = (0, 0, 0) # Texto negro para mejor contraste en dorado
            
        texto_puntos = fuente.render(str(self.puntos), True, color_texto)
        rect = texto_puntos.get_rect(center=(int(self.x), int(self.y)))
        superficie.blit(texto_puntos, rect)


    # Verifica si se hizo clic dentro del círculo
    def clicked(self, pos_x, pos_y):

        # Calcular distancia entre el clic y el centro del círculo
        distancia = math.sqrt((self.x -pos_x)**2 + (self.y - pos_y)**2)

        # Si la distancia es menor o igual al radio, fue un clic válido
        return distancia <= self.radio
