# main.py
import time
from Tablero import *
from Player import *
from Monster import *
from Validation import *
from Game import *



def main():
    # Crear un tablero 5x5
    n = 5
    # Crear un tablero 5x5
    tablero = Tablero(n)

    # Colocar elementos en posiciones aleatorias (por ejemplo, comida y arma)
    tablero.colocar_elemento("comida", (random.randint(0, n-1), random.randint(0, n-1)))
    tablero.colocar_elemento("comida", (random.randint(0, n-1), random.randint(0, n-1)))
    tablero.colocar_elemento("comida", (random.randint(0, n-1), random.randint(0, n-1)))
    tablero.colocar_elemento("comida", (random.randint(0, n-1), random.randint(0, n-1)))
    tablero.colocar_elemento("comida", (random.randint(0, n-1), random.randint(0, n-1)))
    tablero.colocar_elemento("comida", (random.randint(0, n-1), random.randint(0, n-1)))
    tablero.colocar_elemento("comida", (random.randint(0, n-1), random.randint(0, n-1)))
    tablero.colocar_elemento("comida", (random.randint(0, n-1), random.randint(0, n-1)))
    tablero.colocar_elemento("comida", (random.randint(0, n-1), random.randint(0, n-1)))
    tablero.colocar_elemento("comida", (random.randint(0, n-1), random.randint(0, n-1)))
    tablero.colocar_elemento("comida", (random.randint(0, n-1), random.randint(0, n-1)))
    tablero.colocar_elemento("comida", (random.randint(0, n-1), random.randint(0, n-1)))
    
    tablero.colocar_elemento("arma", (random.randint(0, n-1), random.randint(0, n-1)))


    # Crear instancias de Jugador y Monstruo
    jugador = Jugador("Jugador1")
    monstruo = Monstruo()

    # Establecer posición inicial aleatoria para el jugador y el monstruo en una matriz 5x5 (por ejemplo)
    jugador.posicion = (random.randint(0, n-1), random.randint(0, n-1))
    monstruo.posicion = (random.randint(0, n-1), random.randint(0, n-1))

    # Mostrar el estado inicial del juego
    jugador.mostrar_estado()
    monstruo.mostrar_estado()

    # Iniciar el juego
    jugar(jugador, monstruo, tablero)


if __name__ == "__main__":
    main()
