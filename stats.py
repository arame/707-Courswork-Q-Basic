class Stats:
    def __init__(self, episode, steps, explore, exploit, ebsilon):
        #'Episode', 'Steps', 'Explore', 'Exploit', 'Ebsilon'
        self.episode = episode
        self.steps = steps
        self.explore = explore
        self.exploit = exploit
        self.ebsilon = ebsilon