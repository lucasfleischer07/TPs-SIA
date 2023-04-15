import math

import numpy as np
MAX_INT = 255
DELTA = 50

class EachColor:

    MAX_DISTANCE = math.sqrt(3 * math.pow(255, 2))
    
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
         return str(self.red) + " " + str(self.green) + " " + str(self.blue)
         
         
    # Calculo el fitness mediante la distancia euclediana
    def get_fitness(self, target_color):
        distance = self.MAX_DISTANCE - math.sqrt(math.pow(abs(target_color.red - self.red), 2) + math.pow(abs(target_color.green - self.green), 2) + math.pow(abs(target_color.blue - self.blue), 2)) 
        return distance / self.MAX_DISTANCE


    def equals(self, color):
        return (self.red == color.red) and (self.green == color.green) and (self.blue == color.blue)
    
    def __selectMutationAmount(self,value):
        if np.random.uniform() > 0.5 :
            if value <= 205 :
                return value + DELTA
            else:
                return value - DELTA
        else:
            if value >= 50 :
                return value - DELTA
            else:
                return value + DELTA

    def mutate(self):
        color_random = np.random.uniform()
        if color_random <= 0.33 :
            self.red = self.__selectMutationAmount(self.red) 
        elif color_random > 0.33 and color_random <= 0.66 :
            self.green = self.__selectMutationAmount(self.green) 
        else :
            self.blue = self.__selectMutationAmount(self.blue) 

        