# ============================================
# config.py - Configuración del juego
# ============================================

# Configuración de la ventana del juego
ANCHO = 800                     # Ancho de la ventana en píxeles
ALTO = 600                      # Alto de la ventana en píxeles
FPS = 60                        # Fotogramas por segundo

# Colores en formato RGB
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
NARANJA = (255, 165, 0)
PURPURA = (128, 0, 128)
ROSA = (255, 192, 203)
GRIS = (128, 128, 128)
GRIS_CLARO = (200, 200, 200)
CIAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Lista de colores para usar aleatoriamente
COLORES_CIRCULOS = [ROJO, VERDE, AZUL, PURPURA, ROSA, CIAN, MAGENTA]
COLORES_TITULO = [ROJO, NARANJA, AMARILLO, VERDE, AZUL, PURPURA]

ORO = (255, 215, 0)
PROBABILIDAD_ORO = 0.1

# Configuración del juego
TIEMPO_JUEGO = 20           # Duración del juego en segundos
NUM_CIRCULOS = 6            # Número de círculos en pantalla
VELOCIDAD_MIN = -4          # Velocidad mínima de los círculos (negativo para movimiento hacia atrás)
VELOCIDAD_MAX = 4           # Velocidad máxima de los círculos

# Archivo de puntuaciones
ARCHIVO_PUNTUACIONES = "puntuaciones.json"