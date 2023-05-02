from src.multilayerPerceptron import MultilayerPerceptron
from Exercise3.src.stepLayer import StepLayer
from Exercise3.src.tanhLayer import TanhLayer
from Exercise3.src.reluLayer import ReLuLayer
import numpy as np

def main():
    layer1=TanhLayer(2,2)
    layer2=TanhLayer(1,2)
    layers=np.array([layer1,layer2])
    perceptron=MultilayerPerceptron(0.01,layers,10000,0.02,0,0)
    x=np.array([[1,1],[0,0],[1,0],[0,1]])
    y=np.array([[-1],[-1],[1],[1]])
    perceptron.train(x,y)   

if __name__ == "__main__":
    main()