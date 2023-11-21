import random
from Monster import *
from Player import *
from Tablero import *
from FaceDetection import *
from Validation import *
import time
import os
import cv2

cam = cv2.VideoCapture(0)

def jugar(jugador, monstruo, tablero):
    while jugador.vida > 0 and monstruo.vida > 0:
        # Mostrar el estado actual del juego
        cont = 0
        tablero.mostrar_tablero(jugador, monstruo)
        jugador.mostrar_estado()
        monstruo.mostrar_estado()
        
        # Turno del jugador
        while(True):
            time.sleep(0.10)
            accion = ""
            while(True):
                FaceDetection.detect(cam)
                move = FaceDetection.playerAction
                if move in ["up","down","left","right", "open mouth", "smile"]:
                    print(move)
                    break
                FaceDetection.playerAction = None

            if FaceDetection.playerAction == "up":
                accion = "arriba"
                print("si dio arriba")
                
            elif FaceDetection.playerAction == "down":
                accion = "abajo"
            elif FaceDetection.playerAction == "left":
                accion = "izquierda"
            elif FaceDetection.playerAction == "right":
                accion = "derecha"
            elif FaceDetection.playerAction == "open mouth":
                accion = "comer"
            elif FaceDetection.playerAction == "smile":
                accion = "atacar"

            print(accion)
            if accion in ["arriba", "abajo", "izquierda", "derecha"]:
                mover_jugador(jugador, accion, tablero)
                cont = 1
            elif accion == "atacar" and jugador.armas:
                    # El jugador ataca al monstruo con un arma
                atacar_monstruo(jugador, monstruo)
                time.sleep(2)
                cont = 1
            elif accion == "comer" and jugador.comidas:
                    # El jugador ataca al monstruo con un arma
                consumir_comida(jugador, monstruo)
                time.sleep(2)
                cont = 1

            else:
                print("Acción no válida. Puedes moverte (arriba, abajo, izquierda, derecha) o atacar con un arma.")

                    # Turno del monstruo
            mover_monstruo(monstruo, tablero)

            # Verificar interacciones en el tablero
            verificar_interacciones(jugador, monstruo, tablero)

            FaceDetection.playerAction = None
            if cont == 1:
                break
            # Mostrar el resultado del juego
        if jugador.vida <= 0:
            print("¡Has perdido! El monstruo te ha vencido.")
        elif monstruo.vida <= 0:
            print("¡Felicidades! Has vencido al monstruo.")
            

