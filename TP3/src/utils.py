from matplotlib import pyplot as plt, animation

import numpy as np

# Documentation of pyplot
# https://matplotlib.org/stable/api/pyplot_summary.html?highlight=pyplot

# TODO: Transform function to use all weights obtained from training
def plot_graph(points, output, weight):
    fig, ax = plt.subplots()
    fig.suptitle('Step Perceptron Graph')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # ax.set_title('Epoch = ' + str(epoch))

    for i in range(len(points)):
        if output[i] == 1:
            ax.scatter(points[i][0], points[i][1], color='b')
        else:
            ax.scatter(points[i][0], points[i][1], color='r')
    
    min_lim = -2
    max_lim = 2

    ax.set_xlim(min_lim, max_lim)
    ax.set_ylim(min_lim, max_lim)
       

    x = np.linspace(-2, 2, 100)
    #y = -(weight[0] * x + weight[2] / weight[1])
    u = weight[0]
    w = weight[1:]
    a = -w[0] / w[1]

    y = a * x + (u / w[1])
    ax.plot(x, y, color="black")
    plt.show()

def get_accuracy(test_set_result, expected_output):
    correct = 0
    print("Results: ", test_set_result)
    print("Expected: ", expected_output)
    for i in range(len(test_set_result)):
        if (abs(test_set_result[i] - expected_output[i]) < 0.02):
            correct += 1
    return correct / len(test_set_result)

def plot_step(inputs, outputs, weights, min_w):
    # print("weights len: " + str(len(weights)))
    fig, ax = plt.subplots()

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    for i in range(len(inputs)):
        if outputs[i] == 1:
            ax.scatter(inputs[i][0], inputs[i][1], color='b')
        else:
            ax.scatter(inputs[i][0], inputs[i][1], color='r')
    
    x = np.linspace(-1.5, 1.5, 100)
    y = -((min_w[0] * x + min_w[2]) / min_w[1])

    line = ax.plot(x, y, color="black")

    ax.set_title("Step Perceptron Graph")
    def animate(i):
        y1 = -((weights[i][0] * x + weights[i][2]) / weights[i][1])
        ax.plot(x, y1, color="black")

    anim = animation.FuncAnimation(fig, animate, interval=100, frames=len(weights))

    pillow_writer = animation.PillowWriter(fps=20)
    anim.save("step_graph.gif", writer=pillow_writer)
    plt.close()

def plot_errors(errors):
    fig, ax = plt.subplots()

    ax.set_xlabel('Generation')
    ax.set_ylabel('Error')
    ax.set_title('Step Perceptron Error')

    generations = np.array(range(len(errors)))

    ax.set_xlim(0, len(generations))
    ax.set_ylim(0, np.amax(errors))

    ax.plot(generations, errors, color='b')
    plt.show()

def plot_error_in_accuracy(test_results, expected_results):
    fig, ax = plt.subplots()

    errors = abs(test_results - expected_results)
    ax.set_ylabel('Error')
    ax.set_title('Error in Accuracy between Test Results and Expected Results')

    results_count = len(test_results)

    ax.set_xlim(0, results_count)
    ax.set_ylim(0, np.amax(errors))
    
    ax.scatter(range(results_count), errors, color='b')
    plt.show()

def plot_accuracies(epochs,accuracies):
    fig, ax = plt.subplots()

    ax.set_xlabel('Generation')
    ax.set_ylabel('Accuracy')
    ax.set_title('Evolution of Results\' Accuracy by Generation')

    generations = np.array(range(epochs))

    ax.set_xlim(0, len(generations))
    ax.set_ylim(0, np.amax(accuracies))

    ax.plot(generations, accuracies, color='b')
    plt.show()

def escalate(data):
    min_expected = min(data)
    max_expected = max(data)

    data = np.array(data)
    data = 2 * ((data - min_expected) / (max_expected - min_expected)) - 1

    return data