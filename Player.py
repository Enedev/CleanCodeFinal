import random

from Monster import *
from Tablero import *
from Validation import *

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 10
        self.comidas = []
        self.armas = []
        self.posicion = None  # La posición se representará como una tupla (fila, columna)

    def mostrar_estado(self):
        print(f"{self.nombre}: Vida - {self.vida}, Comidas - {self.comidas}, Armas - {self.armas}, Posición - {self.posicion}")

def mover_jugador(jugador, direccion, tablero):
    fila, columna = jugador.posicion

    if direccion == "arriba" and fila > 0:
        jugador.posicion = (fila - 1, columna)
    elif direccion == "abajo" and fila < tablero.tamaño - 1:
        jugador.posicion = (fila + 1, columna)
    elif direccion == "izquierda" and columna > 0:
        jugador.posicion = (fila, columna - 1)
    elif direccion == "derecha" and columna < tablero.tamaño - 1:
        jugador.posicion = (fila, columna + 1)

def consumir_comida(jugador, monstruo):
    # Seleccionar una sola comida aleatoria para el consumo
    if jugador.comidas:
        comida_seleccionada = random.choice(jugador.comidas)
        curacion_valor = comida_seleccionada.get("comida", 0)
        jugador.vida += curacion_valor
        print(f"¡Has consumido {comida_seleccionada}! +{curacion_valor} de vida.")
        jugador.comidas.remove(comida_seleccionada)  # Eliminar la comida después de consumirla
    else:
        print("No tienes comidas para consumir.")

def distancia_monstruo(posicion_jugador, posicion_monstruo):
    fila_jugador, columna_jugador = posicion_jugador
    fila_monstruo, columna_monstruo = posicion_monstruo
    return abs(fila_jugador - fila_monstruo) + abs(columna_jugador - columna_monstruo)

def atacar_monstruo(jugador, monstruo):
    # Seleccionar armas basándose en la distancia al monstruo
    if distancia_monstruo(jugador.posicion, monstruo.posicion) <= 1:
        armas_seleccionadas = [arma for arma in jugador.armas if arma.get("ataque", 0) > 20]
    else:
        armas_seleccionadas = [arma for arma in jugador.armas if arma.get("ataque", 0) <= 20]

    if armas_seleccionadas:
        # Seleccionar una sola arma aleatoria para el ataque
        arma_seleccionada = random.choice(armas_seleccionadas)
        print("Armas seleccionadas:", armas_seleccionadas)
        # Imprimir el contenido del diccionario seleccionado
        print(f"Determinando ataque con arma: {arma_seleccionada}")

        ataque_valor = arma_seleccionada["arma"]
        print("damage :", ataque_valor)

        monstruo.vida -= ataque_valor
        print(f"¡Has atacado al monstruo con {arma_seleccionada}! -{ataque_valor} de vida al monstruo.")
        jugador.armas.remove(arma_seleccionada)  # Eliminar el arma después de usarla

    else:
        print("No puedes atacar al monstruo desde esta distancia o no tienes armas disponibles.")