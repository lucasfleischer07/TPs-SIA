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

# TODO: Falta meter esto del Algoritmo en algun lado
    if(MODE == 2):
        ALGORYTHM = 0
        ALGORYTHM = int(input("\nSeleccione que algoritmo quieres que te lo resuelva\n\t1. A*.\n\t2. BFS.\n\t3. DFS.\n\t4. Greedy.\nAlgoritmo: "))
        while ALGORYTHM != 1 and ALGORYTHM != 2 and ALGORYTHM != 3 and ALGORYTHM != 4:
            ALGORYTHM = int(input("El numero ingresado es incorrecto, por favor ingrese un numero entre el 1 y el 4: "))

    COLORS = 0
    COLORS = int(input("\nSeleccione la cantidad de colores con los que desee jugar (un numero entre 2 y 6): "))
    while COLORS < 2 or COLORS > 6:
        COLORS = int(input("El numero ingresado es incorrecto, por favor un numero entre el 2 y el 6: "))
    

    FillZone(NUM, MODE, COLORS)
    arcade.run()


if __name__ == "__main__":
    main()