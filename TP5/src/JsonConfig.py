import json


class JsonConfig:
    PERCEPTRON_ALGORITHMS = ["multi_layer_perceptron"]
    FUNCTIONS = ['logistic', 'tanh']

    def __init__(self, string):
        config = json.loads(string)
        self.max_iter = int(config.get('max_iter'))
        self.learning_rate = float(config.get('learning_rate'))
        self.betha = float(config.get('betha'))
        self.function = config.get('function')
        self.layers = config.get('layers')
        self.min_error = float(config.get('min_error'))