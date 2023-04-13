import math
MAX_INT = 255

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
    

    def mutate(self):
        self.red = MAX_INT - self.red
        self.green = MAX_INT - self.green
        self.blue = MAX_INT - self.blue