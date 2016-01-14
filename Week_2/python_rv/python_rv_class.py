from my_stats import PMF
import random


class RV(PMF):
    def __init__(self, PMF):
        self.PMF = PMF

    def sample(self):
        rand = random.random()
        p = 0
        for key, val in self.PMF.dict_map.iteritems():
            p += val
            if rand <= p:
                return key

    def all_outcomes(self):
        return sorted(self.PMF.dict_map.keys())

    def pmf(self):
        return self.PMF