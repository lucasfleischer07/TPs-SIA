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
    

    FillZone(NUM, MODE, ALGORYTHM, COLORS)
    arcade.run()

"""
MAIN AUTOMATIZADO
def main():
    run_times = 100
    color_amout = 4
    rows_amount = 4
    mode = 2
    victory_array = []
    time_array = []
    nodes_expanded_array = []
    nodes_border_array = []
    for algorithm in range(1,5)
        victory_array = []
        time_array = []
        nodes_expanded_array = []
        nodes_border_array = []
        for run_time in range(run_times):
            result = FillZone(rows_amount,mode,algorithm,color_amout)
            victory_array.append(result[4])
            time_array.append(result[1])
            nodes_expanded_array.append(result[2])
            nodes_border_array.append(result[3])
        
"""
if __name__ == "__main__":
    main()