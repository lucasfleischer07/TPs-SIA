from src.fillZone import FillZone 
import arcade

def main():
    NUM = 0
    NUM = int(input("Ingrese el numero de filas y columnas que desee para comenzar a jugar: "))
    while NUM < 0:
        NUM = int(input("El numero ingresado es incorrecto, por favor ingrese un numero mayor a 0: "))
    
    MODE = 0
    ALGORYTHM = 0
    MODE = int(input("\nSeleccione el modo de juego\n\t1. Usted juega.\n\t2. Un algoritmo resuelva el juego.\nModo: "))
    while MODE != 1 and MODE != 2:
        MODE = int(input("El numero ingresado es incorrecto, por favor ingrese la opcion 1 o 2: "))

    if(MODE == 2):
        ALGORYTHM = int(input("\nSeleccione que algoritmo quieres que te lo resuelva\n\t1. A*.\n\t2. BFS.\n\t3. DFS.\n\t4. Greedy.\nAlgoritmo: "))
        while ALGORYTHM != 1 and ALGORYTHM != 2 and ALGORYTHM != 3 and ALGORYTHM != 4:
            ALGORYTHM = int(input("El numero ingresado es incorrecto, por favor ingrese un numero del 1 al 4: "))

    HEURISTIC = 0
    if(ALGORYTHM == 1 or ALGORYTHM == 4):
        HEURISTIC = int(input("\nSeleccione que heuristica quieres utilizar\n\t1. Estima cuantos pasos van a faltar para llegar a la celda más lejana del tablero*.\n\t2. Calcula cuántos colores diferentes quedan en el tablero y en base a eso, estima cuántos pasos quedan para finalizar el juego.\n\t3. Desde el color actual, cuantas posiciones van a cambiar con el cambio de color.\nHeuristica: "))
        while HEURISTIC != 1 and HEURISTIC != 2 and HEURISTIC != 3:
            HEURISTIC = int(input("El numero ingresado es incorrecto, por favor ingrese un numero del 1 al 3: "))


    
    COLORS = 0
    COLORS = int(input("\nSeleccione la cantidad de colores con los que desee jugar (un numero entre 2 y 6): "))
    while COLORS < 2 or COLORS > 6:
        COLORS = int(input("El numero ingresado es incorrecto, por favor un numero entre el 2 y el 6: "))
    

    FillZone(NUM, MODE, ALGORYTHM, COLORS, HEURISTIC)
    arcade.run()


if __name__ == "__main__":
    main()