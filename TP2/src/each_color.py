import math

import numpy as np

BITS_NUM = 8
getbinary = lambda x, n: format(x, 'b').zfill(n)

class EachColor:

    MAX_DISTANCE = math.sqrt(3 * math.pow(255, 2))
    
    def __init__(self, red, green, blue,pm):
        self.red = red
        self.green = green
        self.blue = blue
        self.pm = pm
        self.color=(red/255.0,green/255.0,blue/255.0)

    def __str__(self):
         return str(self.red) + " " + str(self.green) + " " + str(self.blue)
         
         
    # Calculo el fitness mediante la distancia euclediana
    def get_fitness(self, target_color):
        distance = self.MAX_DISTANCE - math.sqrt(math.pow(abs(target_color.red - self.red), 2) + math.pow(abs(target_color.green - self.green), 2) + math.pow(abs(target_color.blue - self.blue), 2)) 
        return distance / self.MAX_DISTANCE


    def equals(self, color):
        return (self.red == color.red) and (self.green == color.green) and (self.blue == color.blue)
    
    def __executeMutation(self,value):
        mutated_val = getbinary(value, 8)
        for i in range(8):
            if np.random.uniform() > self.pm:
                if mutated_val[i] == '0':
                    mutated_val = mutated_val[:i] + '1' + mutated_val[i + 1:]
                else:
                    mutated_val = mutated_val[:i] + '0' + mutated_val[i + 1:]
        return int(mutated_val, 2)
            


    def mutate(self):
        self.red = self.__executeMutation(self.red) 
        self.green = self.__executeMutation(self.green) 
        self.blue = self.__executeMutation(self.blue) 

        