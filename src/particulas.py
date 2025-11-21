import pygame
import random
import math

class Particula:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        # Velocidad aleatoria en todas direcciones
        angulo = random.uniform(0, 2 * math.pi)
        velocidad = random.uniform(2, 6)
        self.vx = math.cos(angulo) * velocidad
        self.vy = math.sin(angulo) * velocidad
        
        self.radio = random.randint(3, 6)
        self.vida = 255  # Opacidad/Vida inicial
        self.desvanecimiento = random.randint(10, 20) # Qué tan rápido desaparece

    def actualizar(self):
        self.x += self.vx
        self.y += self.vy
        self.vida -= self.desvanecimiento
        self.radio -= 0.1 # Se hacen más pequeñas
        
    def dibujar(self, pantalla):
        if self.vida > 0 and self.radio > 0:
            # Crear una superficie temporal para la transparencia
            superficie = pygame.Surface((int(self.radio*2), int(self.radio*2)), pygame.SRCALPHA)
            color_con_alpha = (*self.color, int(self.vida))
            pygame.draw.circle(superficie, color_con_alpha, (int(self.radio), int(self.radio)), int(self.radio))
            pantalla.blit(superficie, (int(self.x - self.radio), int(self.y - self.radio)))

class SistemaParticulas:
    def __init__(self):
        self.particulas = []

    def lanzar_explosion(self, x, y, color):
        # Crear entre 10 y 20 partículas
        for _ in range(random.randint(10, 20)):
            self.particulas.append(Particula(x, y, color))

    def actualizar(self):
        # Actualizar partículas y eliminar las muertas
        for p in self.particulas[:]:
            p.actualizar()
            if p.vida <= 0 or p.radio <= 0:
                self.particulas.remove(p)

    def dibujar(self, pantalla):
        for p in self.particulas:
            p.dibujar(pantalla)
