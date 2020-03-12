class Stats:
    def __init__(self, episode, steps, explore, exploit, ebsilon):
        self.episode = episode
        self.ebsilon = ebsilon
        self.steps = steps
        self.explore = explore
        self.exploit = exploit
