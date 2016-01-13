class PMF(object):
    def __init__(self, prob_map):
        self.dict_map = prob_map
        self.normalizer()

    def prob(self, val):
        return self.dict_map[val]

    def print_pmf(self):
        return self.dict_map.items()

    def set(self, key_val_tup):
        self.dict_map[key_val_tup[0]] = float(key_val_tup[1])
        self.normalizer()

    def normalizer(self):
        normalizer = sum(self.dict_map.values())
        for item in self.print_pmf():
            self.dict_map[item[0]] = item[1]/normalizer
