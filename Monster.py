import random
from Player import *
from Tablero import *
from Validation import *

class Monstruo:
    def __init__(self):
        self.vida = 100
        self.posicion = None

    def mostrar_estado(self):
        print(f"Monstruo: Vida - {self.vida}, Posición - {self.posicion}")

def distancia_monstruo(posicion_jugador, posicion_monstruo):
    fila_jugador, columna_jugador = posicion_jugador
    fila_monstruo, columna_monstruo = posicion_monstruo
    return abs(fila_jugador - fila_monstruo) + abs(columna_jugador - columna_monstruo)

def teletransportar_monstruo(monstruo, tablero, jugador):
    # Teletransportar al monstruo a una posición aleatoria lejana
    nueva_posicion = (random.randint(0, tablero.tamaño - 1), random.randint(0, tablero.tamaño - 1))

    while tablero.matriz[nueva_posicion[0]][nueva_posicion[1]] in ["comida", "arma"] or distancia_monstruo(nueva_posicion, jugador.posicion) <= 3:
        nueva_posicion = (random.randint(0, tablero.tamaño - 1), random.randint(0, tablero.tamaño - 1))

    monstruo.posicion = nueva_posicion
    print("¡El monstruo se ha teletransportado a una posición alejada!")

def mover_monstruo(monstruo, tablero):
     # Direcciones posibles: arriba, abajo, izquierda, derecha
    direcciones = ["arriba", "abajo", "izquierda", "derecha"]

    # Seleccionar una dirección aleatoria
    direccion = random.choice(direcciones)

    # Obtener la posición actual del monstruo
    fila, columna = monstruo.posicion

    # Calcular la nueva posición basada en la dirección seleccionada
    if direccion == "arriba" and fila > 0:
        monstruo.posicion = (fila - 1, columna)
    elif direccion == "abajo" and fila < tablero.tamaño - 1:
        monstruo.posicion = (fila + 1, columna)
    elif direccion == "izquierda" and columna > 0:
        monstruo.posicion = (fila, columna - 1)
    elif direccion == "derecha" and columna < tablero.tamaño - 1:
        monstruo.posicion = (fila, columna + 1)
