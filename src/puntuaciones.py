# ============================================
# puntuaciones.py - Sistema de puntuaciones
# ============================================

import json
import os
from datetime import datetime
from src.config import ARCHIVO_PUNTUACIONES

# Gestiona las puntuaciones del juego
class SistemaPuntuaciones:
    
    # Inicializa el sistema y carga las puntuaciones
    def __init__(self, archivo=ARCHIVO_PUNTUACIONES):
        """."""
        self.archivo = archivo  # ← IMPORTANTE: Esto PRIMERO
        self.puntuaciones = self.cargar_puntuaciones()  # ← Luego esto
    

    # Carga las puntuaciones desde el archivo JSON
    def cargar_puntuaciones(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    

    #Guarda las puntuaciones en el archivo JSON
    def guardar_puntuaciones(self):
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                json.dump(self.puntuaciones, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar puntuaciones: {e}")
    

    # Agrega una nueva puntuación al sistema o actualiza si es mejor
    def agregar_puntuacion(self, nombre, curso, puntuacion, clicks_fallados):
        # Buscar si el usuario ya existe
        usuario_existente = None
        for p in self.puntuaciones:
            if p["nombre"] == nombre and p["curso"] == curso:
                usuario_existente = p
                break
        
        if usuario_existente:
            # Si existe, solo actualizamos si la nueva puntuación es mejor
            if puntuacion > usuario_existente["puntuacion"]:
                usuario_existente["puntuacion"] = puntuacion
                usuario_existente["clicks_fallados"] = clicks_fallados
                usuario_existente["fecha"] = datetime.now().strftime("%d/%m/%Y %H:%M")
                # Reordenamos la lista
                self.puntuaciones.sort(key=lambda x: x["puntuacion"], reverse=True)
                self.guardar_puntuaciones()
        else:
            # Si no existe, lo agregamos como nuevo
            nueva_puntuacion = {
                "nombre": nombre,
                "curso": curso,
                "puntuacion": puntuacion,
                "clicks_fallados": clicks_fallados,
                "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            self.puntuaciones.append(nueva_puntuacion)
            self.puntuaciones.sort(key=lambda x: x["puntuacion"], reverse=True)
            self.guardar_puntuaciones()


    # Obtiene la posición de una puntuación en el ranking
    def obtener_posicion(self, puntuacion):
        for i, p in enumerate(self.puntuaciones):
            if puntuacion >= p["puntuacion"]:
                return i + 1
        return len(self.puntuaciones) + 1
    

    # Obtiene el top 10 de puntuaciones
    def obtener_top10(self):
        return self.puntuaciones[:10]
    

    #Obtiene el número total de jugadores
    def obtener_total_jugadores(self):
        return len(self.puntuaciones)