import random
from Game import *
from Monster import *
from Player import *
from Validation import *

class Tablero:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.matriz = [[None for _ in range(tamaño)] for _ in range(tamaño)]

    def mostrar_tablero(self, jugador, monstruo):
        for fila in range(self.tamaño):
            for columna in range(self.tamaño):
                if (fila, columna) == jugador.posicion:
                    print("😇", end=" ")
                elif (fila, columna) == monstruo.posicion:
                    print("🤡", end=" ")
                elif self.matriz[fila][columna] == "comida":
                    print("🍔", end=" ")
                elif self.matriz[fila][columna] == "arma":
                    print("⚔️", end=" ")
                else:
                    print("-", end=" ")
            print()

    def colocar_elemento(self, elemento, posicion):
        fila, columna = posicion
        self.matriz[fila][columna] = elemento
