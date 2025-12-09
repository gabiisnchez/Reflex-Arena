# ============================================
# config.py - Configuración del juego
# ============================================

# Configuración de la ventana del juego
ANCHO = 1024                    # Ancho de la ventana en píxeles
ALTO = 900                      # Alto de la ventana en píxeles
FPS = 60                        # Fotogramas por segundo

# Colores en formato RGB
# Colores en formato RGB
NEGRO = (26, 26, 46)        # Deep Blue Background
BLANCO = (255, 255, 255)
ROJO = (233, 69, 96)        # Highlights / Errors
VERDE = (0, 255, 127)       # Success
AZUL = (15, 52, 96)         # Deep Navy Accent
AMARILLO = (255, 215, 0)    # Gold
NARANJA = (255, 128, 0)
PURPURA = (138, 43, 226)
ROSA = (255, 105, 180)
GRIS = (128, 128, 128)
GRIS_CLARO = (160, 160, 160)
CIAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Paleta Moderna
COLOR_FONDO = (26, 26, 46)      # #1a1a2e
COLOR_PANEL = (22, 33, 62)      # #16213e
COLOR_ACCENTO = (15, 52, 96)    # #0f3460
COLOR_TEXTO = (255, 255, 255)
COLOR_RESALTE = (233, 69, 96)   # #e94560

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