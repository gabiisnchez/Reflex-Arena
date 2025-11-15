# ============================================
# puntuaciones.py - Sistema de puntuaciones
# ============================================

import json                                 # Para manejar archivos JSON
import os                                   # Para verificar si el archivo existe
from datetime import datetime               # Para registrar la fecha y la hora de la puntuación
from config import ARCHIVO_PUNTUACIONES

class SistemaPuntuaciones:
    """
    Gestiona las puntuaciones del juego.
    
    Carga, guarda, ordena y consulta las puntuaciones almacenadas en JSON.
    """
    
    # Constructor: Inicializa el sistema y carga las puntuaciones
    def __init__(self, archivo=ARCHIVO_PUNTUACIONES):

        # Verifica si el archivo existe
        if os.path.exists(self.archivo):
            try:

                # Intenta abrir y leer el archivo JSON
                with open(self.archivo, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:

                # Si hay cualquier error, retornar lista vacía
                return []
            
            # Si el archivo no existe, retornar lista vacía
            return[]
        

    # Guarda lass puntuaciones en el archivo JSON
    def guardar_puntuaciones(self):
        try:

            # Intenta escribir el archivo
            with open(self.archivo, 'w', encoding='utf-8') as f:
                json.dump(self.puntuaciones, f, indent=4, ensure_ascii=False)
        except Exception as e:

            # Si hay un error, mostrarlo
            print(f"Error al guardar las puntuaciones: {e}")


    # Agrega una nueva puntuación al sistema
    def agregar_puntuaciones(self, nombre, curso, puntuación, clicks_fallados):

        # Crar diccionario con la nueva puntuación
        nueva_puntuacion = {
            "nombre": nombre,
            "curso": curso, 
            "puntuación": puntuación, 
            "clicks_fallados": clicks_fallados, 
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        # Agregar a la lista
        self.puntuaciones.append(nueva_puntuacion)

        # Ordenar por puntuación (mayor a menor)
        self.puntuaciones.sort(key=lambda x: x["puntuacion"], reverse=True)

        # Guardar en el archivo
        self.guardar_puntuaciones()


    # Obtiene la posición de una puntuación en el ranking
    def obtener_posicion(self, puntuacion):
        
        # Recorrer todas las puntuaciones guardadas
        for i, p in enumerate(self.puntuaciones):

            # Si encontramos una puntuación igual o menror
            if puntuacion >= p["puntuacion"]:
                return i + 1
            
        # Si no se encontró, es la última posición
        return len(self.puntuaciones) + 1
    

    # Obtiene el top 10 de puntuaciones.
    def obtener_top10(self):
        return self.puntuaciones[:10]
    

    # Obtiene el número total de jugadores.
    def obtener_total_jugadores(self):
        return len(self.puntuaciones)