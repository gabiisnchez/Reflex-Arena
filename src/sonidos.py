# ============================================
# sonidos.py - Sistema de sonidos del juego
# ============================================

import pygame
import os

# Gestiona los sonidos principales del juego
class GestorSonidos:

    # Inicializa el mixer y carga los sonidos
    def __init__(self):

        # Inicializar el mixer de audio
        pygame.mixer.init()

        # Diccionario para los sonidos
        self.sonidos = {}

        # Cargar los sonidos
        self.cargar_sonidos()

        # Volumen general de los sonidos
        self.volumen = 0.5

    # Carga los 4 archivos de sonido
    def cargar_sonidos(self):

        base_path = "assets/sounds/"

        archivos = {
            "click": "click.mp3",
            "fail": "fail.mp3",
            "tictac": "tictac.mp3",
            "record": "record.mp3"
        }

        for nombre, archivo in archivos.items():
            ruta = os.path.join(base_path, archivo)
            try:
                self.sonidos[nombre] = pygame.mixer.Sound(ruta)
                self.sonidos[nombre].set_volume(self.volumen)
                print(f"Sonido {nombre} cargado exitosamente.")
            except pygame.error as e:
                print(f"Error al cargar el sonido {nombre}: {e}")
                self.sonidos[nombre] = None

    # Reproduce un sonido
    def reproducir(self, nombre):
        if nombre in self.sonidos and self.sonidos[nombre] is not None:
            self.sonidos[nombre].play()

    # Ajusta el volumen (0.0 a 1.0)
    def set_volumen(self, volumen):
        self.volumen = max(0.0, min(1.0, volumen))
        for sonido in self.sonidos.values():
            if sonido is not None:
                sonido.set_volume(self.volumen)