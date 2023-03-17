from src.fillZone import FillZone 
import arcade

def main():
    # NUM = 0
    # NUM = int(input("Ingrese el numero de filas y columnas que desee para comenzar a jugar: "))
    
    # while NUM < 0:
    #     NUM = int(input("El numero ingresado es incorrecto, por favor ingrese un numero mayor a 0"))
    
    # MODE = int(input("Seleccione el modo de juego\n\t1. Usted juega.\n\t2. Un algoritmo resuelva el juego.\n\nModo: "))
    
    # while MODE != 1 and MODE != 2:
    #     MODE = int(input("El numero ingresado es incorrecto, por favor ingrese la opcion 1 o 2: "))
    
    # result = FillZone(NUM, MODE)
    result = FillZone()
    soluton = arcade.run()


if __name__ == "__main__":
    main()