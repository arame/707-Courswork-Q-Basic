import matplotlib.pyplot as plt
import numpy as np
from stats import Stats
from hyperparameters import Hyperparam

class ShowStats:
    def __init__(self):
        self.fig = plt.figure()

    def invoke(self, listStats):
        self.fig.add_subplot(111)
        x_label_text = f"Episode # (learning rate = {Hyperparam.learning_rate}, discount factor = {Hyperparam.discount_factor})"
        steps = []
        for row in listStats:
            steps.append(row.steps)
        episodes = np.arange(1, len(steps)+1)
        plt.plot(episodes, steps)
        plt.ylabel('Steps')
        plt.xlabel(x_label_text)
        plt.show()
