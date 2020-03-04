

class Hyperparam:
    epsilon = 0.01
    epsilon_increase = 1.0001
    epsilon_threshold = 0.7
    learning_rate = 0.5
    discount_factor = 0.5
    noOfEpisodes = 500

    @staticmethod
    def display():
        print("The Hyperparameters")
        print("-------------------")
        print(f"Threshold for exploitation (epsilon) = {Hyperparam.epsilon}")
        print(f"epsilon increase = {Hyperparam.epsilon_increase}")
        print(f"Threshold to stop epsilon changing (to abandon the learning) = {Hyperparam.epsilon_threshold}")
        print(f"learning rate (alpha) = {Hyperparam.learning_rate}")
        print(f"discount factor (gamma) = {Hyperparam.discount_factor}")
        print(f"number of episodes = {Hyperparam.noOfEpisodes}")