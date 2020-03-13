

class Hyperparam:
    epsilon = 0.9
    epsilon_decay = 0.9999
    learning_rate = 0.5
    discount_factor = 0.99
    noOfEpisodes = 5000

    @staticmethod
    def display():
        print("The Hyperparameters")    
        print("-------------------")
        print(f"Threshold for exploitation (epsilon) = {Hyperparam.epsilon}")
        print(f"epsilon decay = {Hyperparam.epsilon_decay}")
        print(f"learning rate (alpha) = {Hyperparam.learning_rate}")
        print(f"discount factor (gamma) = {Hyperparam.discount_factor}")
        print(f"number of episodes = {Hyperparam.noOfEpisodes}")