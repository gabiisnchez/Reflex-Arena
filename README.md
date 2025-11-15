# ⚡ Reflex Arena

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-00D1B2?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**Juego arcade de reflejos y precisión desarrollado en Python con Pygame**

*Creado para el Interciclo - MEDAC Sevilla Este 2025*

[Características](#-características) •
[Instalación](#-instalación) •
[Cómo Jugar](#-cómo-jugar) •
[Configuración](#-configuración) •
[Contribuir](#-contribuir)

---

</div>

## 📖 Descripción

**ReflexArena** es un juego arcade competitivo que desafía tus reflejos y precisión. Los jugadores deben hacer clic en círculos en movimiento durante 20 segundos intensos, compitiendo por alcanzar el TOP 10 del ranking. 

Perfecto para eventos escolares, competiciones amistosas y torneos entre estudiantes.

### ✨ Lo que hace especial a Reflex Arena:

- 🎯 **Desafío único**: Un solo nivel de dificultad para que todos compitan en igualdad de condiciones
- 🏆 **Sistema de ranking**: Puntuaciones persistentes con TOP 10 en tiempo real
- 👥 **Registro de jugadores**: Identifica participantes por nombre y curso
- 🎨 **Interfaz atractiva**: Colores vibrantes y animaciones fluidas
- ⚡ **Partidas rápidas**: 20 segundos de juego intenso
- 💾 **Persistencia de datos**: Todas las puntuaciones se guardan automáticamente

---

## 🎮 Características

### 🎯 Mecánicas de Juego

- **6 círculos simultáneos** moviéndose por la pantalla
- **Sistema de puntos variable**: Los círculos más pequeños valen más puntos (1-6 pts)
- **Penalización por fallos**: -1 punto por cada click fallado
- **Velocidad desafiante**: Círculos con diferentes velocidades y trayectorias
- **Rebote dinámico**: Los círculos rebotan en los bordes de forma realista

### 🏆 Sistema de Ranking

- **TOP 10 visible**: Muestra los mejores jugadores en tiempo real
- **Posición instantánea**: Sabes al terminar qué posición ocupas
- **Medallas**: 🥇🥈🥉 para los 3 mejores jugadores
- **Historial completo**: Todas las partidas se guardan con fecha y hora
- **Estadísticas detalladas**: Nombre, curso, puntuación y clicks fallados

### 🎨 Interfaz

- **Pantalla de registro**: Introduce nombre y curso antes de jugar
- **Pantalla de inicio**: Información del desafío y botón de inicio
- **Pantalla de juego**: Contador de tiempo y puntos en vivo
- **Pantalla final**: Resultados, posición en el ranking y TOP 10
- **Efectos visuales**: Colores dinámicos, cursor parpadeante, hover effects

---

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación Paso a Paso

**1. Clona o descarga el repositorio:**
```bash
git clone https://github.com/gabiisnchez/Reflex-Arena.git
cd Reflex-Arena
```

O descarga el ZIP y extráelo en tu ordenador.

**2. Instala las dependencias:**
```bash
pip install pygame
```

En Mac/Linux usa:
```bash
pip3 install pygame
```

**3. Verifica la instalación:**
```bash
python -c "import pygame; print('Pygame instalado correctamente')"
```

**4. Ejecuta el juego:**
```bash
python main.py
```

¡Y listo! El juego debería abrirse automáticamente 🎉

---

## 📁 Estructura del Proyecto
```
Reflex-Arena/
│
├── config.py              # Configuración global y constantes
├── puntuaciones.py        # Sistema de gestión de puntuaciones
├── circulo.py             # Lógica de los círculos (movimiento, colisión)
├── ui.py                  # Funciones de interfaz (textos, botones, inputs)
├── pantallas.py           # Clases de todas las pantallas del juego
├── main.py                # Punto de entrada principal
├── puntuaciones.json      # Datos de puntuaciones (se crea automáticamente)
└── README.md              # Este archivo
```

### Descripción de Módulos

| Archivo | Descripción |
|---------|-------------|
| `config.py` | Constantes globales: colores, dimensiones, velocidades, configuración del juego |
| `puntuaciones.py` | Gestión de puntuaciones: carga, guardado, ranking, posiciones |
| `circulo.py` | Clase `Circulo`: movimiento, rebote, colisión, renderizado |
| `ui.py` | Funciones de UI: dibujar textos, botones, cajas de input |
| `pantallas.py` | Clases: `PantallaRegistro`, `PantallaInicio`, `PantallaJuego`, `PantallaFinal` |
| `main.py` | Bucle principal del juego y gestión del flujo entre pantallas |

---

## 🎯 Cómo Jugar

### Paso 1: Registro
Al abrir el juego, introduce tu **nombre** y **curso** (ej: "Carlos", "2º DAM")

### Paso 2: Iniciar el Desafío
Presiona el botón **"¡EMPEZAR DESAFÍO!"** cuando estés listo

### Paso 3: ¡Juega!
- Haz clic en los círculos que aparecen en pantalla
- Los círculos **pequeños** valen **más puntos** (hasta 6 pts)
- Los círculos **grandes** valen **menos puntos** (1-2 pts)
- Evita hacer clicks fallados (pierdes 1 punto)
- Tienes **20 segundos** para conseguir la mayor puntuación posible

### Paso 4: Resultados
Al terminar verás:
- Tu puntuación final
- Tu posición en el ranking
- El TOP 10 actualizado con tu resultado
- Opción de jugar otra vez o salir

---

## ⚙️ Configuración

Puedes ajustar el juego editando el archivo `config.py`:

### Ajustar Dificultad
```python
# Tiempo de juego (en segundos)
TIEMPO_JUEGO = 20  # Aumenta para más tiempo

# Número de círculos en pantalla
NUM_CIRCULOS = 6   # Reduce para facilitar

# Velocidad de los círculos
VELOCIDAD_MIN = -4  # Reduce el número absoluto para hacerlo más lento
VELOCIDAD_MAX = 4
```

### Modificar Colores
```python
# Cambia cualquier color (formato RGB)
VERDE = (50, 255, 50)
AZUL = (50, 150, 255)
# ... etc
```

### Ajustar Pantalla
```python
# Dimensiones de la ventana
ANCHO = 800  # Ancho en píxeles
ALTO = 600   # Alto en píxeles

# Fotogramas por segundo
FPS = 60  # Reduce a 30 si va lento
```

### Modo Pantalla Completa (opcional)

En `main.py`, línea 14, cambia:
```python
# De esto:
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# A esto:
pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
```

---

## 📊 Sistema de Puntuación

### Valores por Círculo

| Tamaño del Círculo | Radio (px) | Puntos |
|-------------------|-----------|---------|
| Muy Pequeño 🔴    | 20-29     | 6 puntos |
| Pequeño 🟠        | 30-39     | 4-5 puntos |
| Mediano 🟡        | 40-49     | 2-3 puntos |
| Grande 🟢         | 50        | 1 punto |

### Penalizaciones

- ❌ **Click fallado**: -1 punto
- ✅ **Click acertado**: +1 a +6 puntos (según tamaño)

### Consejos para Alto Puntaje

1. 🎯 **Prioriza círculos pequeños**: Valen hasta 6 veces más
2. ⚡ **Sé preciso**: Cada click fallado resta puntos
3. 👀 **Predice trayectorias**: Anticipa dónde estarán los círculos
4. 🕐 **Mantén la calma**: La velocidad sin precisión no sirve
5. 🎮 **Practica**: Conoce los patrones de rebote

---

## 🏆 Para Jornadas de Puertas Abiertas

### Preparación del Evento

**1. Resetear Ranking Diario:**
```bash
# Elimina el archivo de puntuaciones cada día
rm puntuaciones.json
```

**2. Configurar Pantalla:**
- Usa un monitor grande o proyector
- Activa el modo pantalla completa
- Asegura buena visibilidad del TOP 10

**3. Promoción del Juego:**
```markdown
📢 ¡DESAFÍO DE REFLEJOS!
⏱️ 20 segundos de adrenalina
🏆 Compite por el TOP 10
```

**4. Estadísticas del Evento:**

El archivo `puntuaciones.json` contiene todos los datos. Puedes analizarlo para:
- Ver el curso con mejor promedio
- Encontrar el récord del día
- Contar participantes totales
- Identificar tendencias

### Script de Análisis (Bonus)
```python
# analizar_resultados.py
import json

with open('puntuaciones.json', 'r') as f:
    datos = json.load(f)

print(f"📊 Total de participantes: {len(datos)}")
print(f"🏆 Récord del evento: {datos[0]['puntuacion']} pts")
print(f"👑 Ganador: {datos[0]['nombre']} ({datos[0]['curso']})")

# Promedio por curso
cursos = {}
for p in datos:
    curso = p['curso']
    if curso not in cursos:
        cursos[curso] = []
    cursos[curso].append(p['puntuacion'])

print("\n📚 Promedio por curso:")
for curso, puntos in cursos.items():
    print(f"   {curso}: {sum(puntos)/len(puntos):.1f} pts")
```

---

## 🛠️ Solución de Problemas

### El juego no arranca

**Problema:** `ModuleNotFoundError: No module named 'pygame'`
```bash
# Solución:
pip install pygame --upgrade
```

**Problema:** `python: command not found`
```bash
# Solución: Usa python3
python3 main.py
```

### El juego va lento

**Solución:** Reduce el FPS en `config.py`:
```python
FPS = 30  # En lugar de 60
```

### No se guardan las puntuaciones

**Problema:** Permisos de escritura
```bash
# Solución: Ejecuta desde una carpeta con permisos
# o ejecuta como administrador
```

### Los emojis no se ven

**Problema:** Fuente del sistema sin soporte Unicode

**Solución:** El código actual usa render básico y funciona en la mayoría de sistemas. Si tienes problemas, puedes eliminar los emojis del código en `pantallas.py`.

### Pantalla muy grande/pequeña

**Solución:** Ajusta en `config.py`:
```python
ANCHO = 1024  # Tu ancho preferido
ALTO = 768    # Tu alto preferido
```

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si quieres mejorar el juego:

### Cómo Contribuir

1. **Fork** el proyecto
2. Crea una **rama** para tu feature (`git checkout -b feature/MiMejora`)
3. **Commit** tus cambios (`git commit -m 'Añade nueva característica'`)
4. **Push** a la rama (`git push origin feature/MiMejora`)
5. Abre un **Pull Request**

### Reportar Bugs

Si encuentras un bug, abre un **Issue** con:
- Descripción del problema
- Pasos para reproducirlo
- Sistema operativo y versión de Python
- Capturas de pantalla (si aplica)

---

## 📜 Licencia

Este proyecto está bajo la Licencia MIT.
```
MIT License

Copyright (c) 2025 ReflexArena

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
de este software y archivos de documentación asociados (el "Software"), para usar
el Software sin restricciones, incluyendo sin limitación los derechos de usar,
copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender copias
del Software, y permitir a las personas a quienes se les proporcione el Software
hacer lo mismo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permisos se incluirán en todas
las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O
IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS
AUTORES O TITULARES DEL COPYRIGHT SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN,
DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O
DE OTRO MODO, DERIVADAS DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO
U OTROS TRATOS EN EL SOFTWARE.
```

---

## 👨‍💻 Autor

Desarrollado con ❤️ para el **Interciclo 2025**

**Contacto:**
- GitHub: [@gabiisnchez](https://github.com/gabiisnchez)
- Email: gabiisnchez@proton.me

---

## 🙏 Agradecimientos

- **Pygame Community** - Por la excelente documentación y soporte
- **Python Software Foundation** - Por crear un lenguaje tan accesible
- **Estudiantes del Instituto** - Por probar y dar feedback
- **Profesores** - Por el apoyo en las jornadas

---

## 📸 Screenshots

### Pantalla de Registro
![Registro](https://via.placeholder.com/800x600/000000/FFFFFF?text=Pantalla+de+Registro)

*Introduce tu nombre y curso para comenzar*

### Pantalla de Juego
![Juego](https://via.placeholder.com/800x600/000000/FFFFFF?text=Pantalla+de+Juego)

*20 segundos de pura adrenalina haciendo clic en círculos en movimiento*

### Pantalla de Resultados
![Resultados](https://via.placeholder.com/800x600/000000/FFFFFF?text=Resultados+y+TOP+10)

*Visualiza tu posición en el ranking y el TOP 10 actualizado*

---

## 🎓 Contexto Educativo

Este proyecto fue desarrollado como parte del **Interciclo** del instituto MEDAC Sevilla Este, con los objetivos de:

- 🎮 Demostrar aplicaciones prácticas de la programación
- 🤝 Fomentar la competencia sana entre estudiantes
- 💻 Inspirar a futuros estudiantes a aprender programación
- 🎯 Desarrollar habilidades de pensamiento lógico y reflejos

**Tecnologías aprendidas:**
- Programación orientada a objetos (POO)
- Gestión de eventos y bucles de juego
- Manejo de archivos JSON
- Diseño de interfaces de usuario
- Matemáticas aplicadas (colisiones, trayectorias)

---


## ❓ FAQ

**P: ¿Puedo modificar el juego para mi instituto?**

R: ¡Sí! El proyecto es open source bajo licencia MIT. Personalízalo como quieras.

**P: ¿Funciona en Mac/Linux?**

R: Sí, Pygame es multiplataforma. Solo asegúrate de usar `python3` y `pip3`.

**P: ¿Cómo reseteo el ranking?**

R: Simplemente elimina el archivo `puntuaciones.json`.

**P: ¿Puedo cambiar los colores?**

R: Sí, edita los valores RGB en `config.py`.

**P: ¿Qué puntuación es buena?**

R: +80 es excelente, +50 es muy bueno, +30 es bueno.

**P: ¿Puedo crear un ejecutable?**

R: Sí, usa PyInstaller: `pyinstaller --onefile --windowed main.py`

---

<div align="center">

**⭐ Si te gusta el proyecto, dale una estrella en GitHub ⭐**

Hecho con 💙 y ☕ | [Reportar Bug](https://github.com/tuusuario/reflexarena/issues) | [Solicitar Feature](https://github.com/tuusuario/reflexarena/issues)

</div>