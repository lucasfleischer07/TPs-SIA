from src.fillZone import FillZone 
import arcade

def main():
    NUM = 0
    NUM = int(input("Ingrese el numero de filas y columnas que desee para comenzar a jugar: "))
    while NUM < 0:
        NUM = int(input("El numero ingresado es incorrecto, por favor ingrese un numero mayor a 0: "))
    
    MODE = 0
    MODE = int(input("\nSeleccione el modo de juego\n\t1. Usted juega.\n\t2. Un algoritmo resuelva el juego.\nModo: "))
    while MODE != 1 and MODE != 2:
        MODE = int(input("El numero ingresado es incorrecto, por favor ingrese la opcion 1 o 2: "))

    COLORS = 0
    COLORS = int(input("\nSeleccione la cantidad de colores con los que desee jugar (un numero entre 2 y 6): "))
    while COLORS < 2 or COLORS > 6:
        COLORS = int(input("El numero ingresado es incorrecto, por favor un numero entre el 2 y el 6: "))
    
    FillZone(NUM, MODE, COLORS)
    arcade.run()


if __name__ == "__main__":
    main()