# ============================================
# circulo.py - Clase Circulo
# ============================================

import random       # Para generar número aleatorios
import math         # Para operaciones matemáticas
import pygame
from config import COLORES_CIRCULOS, BLANCO, VELOCIDAD_MIN, VELOCIDAD_MAX

class Circulo:
    """
    Representa un círculo en el juego.
    
    Cada círculo tiene posición, tamaño, color, velocidad y valor en puntos.
    Se mueve rebotando en los bordes y puede detectar si fue clickeado.
    """

    def __init__(self, ancho, alto):
        # Constructor que inicializar un círculo con valores aleatorios

        # Guardar dimensiones de la pantalla
        self.ancho = ancho
        self.alto = alto

        # Radio aleatorio entre 20 y 50 píxeles
        self.radio = random.randint(20, 50)

        # Posición X aleatoria (pero sin salirse de la pantalla)
        self.x = random.randint(self.radio, ancho - self.radio)

        # Posición Y aleatorio (empezando desde y=100 para dejar espacio arriba)
        self.y = random.randint(100 + self.radio, alto -self.radio)

        # Color aleatorio de la lista de colores
        self.color = random.choice(COLORES_CIRCULOS)

        # Velocidades aleatorias (excluyendo 0)
        velocidades = [i for i in range(VELOCIDAD_MIN, VELOCIDAD_MAX + 1) if i != 0]
        self.velocidad_x = random.choice(velocidades)
        self.velocidad_y = random.choice(velocidades)

        # Calcular puntos según tamaño (más pequeño = más puntos)
        self.puntos = max(1, 6 - (self.radio // 10))

    def mover(self):
        # Mueve el círculo según su velocidad y lo hace rebotar en los bordes

        # Actualizar posición
        self.x += self.velocidad_x
        self.y += self.velocidad_y

        # Rebotasr en bordes horizontales
        if self.x - self.radio <= 0 or self.x + self.radio >= self.ancho:
            self.velocidad_x *= -1 # Invertir dirección X

        # Rebotar en bordes verticales
        if self.y - self.radio <= 100 or self.y + self.radio >= self.alto:
            self.velocidad_y *= -1 # Invertir dirección Y

    def dibujar(self, superficie, fuente):
        # Dibuja el círculo en la pantalla con su número de puntos

        # Dibujar círculo relleno
        pygame.draw.circle(superficie, self.color, (int)(self.x), (int)(self.y), self.radio)

        # Dibujar borde blanco
        pygame.draw.circle(superficie, BLANCO, (int)(self.x), (int)(self.y), self.radio, 3)

        # Dibujar número de puntos en el centro
        texto_puntos = fuente.render(str(self.puntos), True, BLANCO)
        rect = texto_puntos.get_rect(center=(int(self.x), int(self.y)))
        superficie.blit(texto_puntos, rect)

    def clicked(self, pos_x, pos_y):
        # Verifica si se hizo clic dentro del círculo

        # Calcular distancia entre el clic y el centro del círculo
        distancia = math.sqrt((self.x -pos_x)**2 + (self.y - pos_y)**2)

        # Si la distancia es menor o igual al radio, fue un clic válido
        return distancia <= self.radio
