from src.multilayerPerceptron import MultilayerPerceptron
from Exercise3.src.stepLayer import StepLayer
import numpy as np
def main():
    layer1=StepLayer(2,2)
    layer2=StepLayer(1,2)
    layers=np.array([layer1,layer2])
    perceptron=MultilayerPerceptron(0.01,layers,10000,0.02,0,0)
    x=np.array([[1,1],[0,0],[1,0],[0,1]])
    y=np.array([[-1],[-1],[1],[1]])
    perceptron.train(x,y)

if __name__ == "__main__":
    main()