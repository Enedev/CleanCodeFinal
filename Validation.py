from Game import *
from Monster import *
from Player import *
from Tablero import *
import random

def verificar_interacciones(jugador, monstruo, tablero):
    fila_jugador, columna_jugador = jugador.posicion
    fila_monstruo, columna_monstruo = monstruo.posicion

    # Verificar si el jugador y el monstruo están en la misma celda
    if (fila_jugador, columna_jugador) == (fila_monstruo, columna_monstruo):
        # El monstruo ataca al jugador
        jugador.vida -= 25
        print("¡El monstruo te ha atacado y te ha quitado 25 de vida!")

    # Verificar si hay elementos en la celda del jugador
    elemento = tablero.matriz[fila_jugador][columna_jugador]
    if elemento == "comida":
        curacion = random.randint(10, 30)
        jugador.comidas.append({"comida": curacion})
        print("¡Has encontrado comida! Agregada al inventario.")
    elif elemento == "arma":
        ataque = random.randint(20, 60)
        jugador.armas.append({"arma": ataque})
        print("¡Has encontrado un arma! Agregada al inventario.")

    # Limpiar la celda después de recoger el elemento
    tablero.matriz[fila_jugador][columna_jugador] = None

