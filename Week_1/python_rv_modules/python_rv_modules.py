from random import random

def random_variable(pmf):
    '''
    INPUT: dictionary
    OUTPUT: one of the keys of the dictionary

    Return one of the keys of the dictionary according to the given probabilities. You may assume the probabilities sum to 1.
    '''
    random_num = random()
    cum_prob = 0.0
    for value, prob in pmf.iteritems():
        cum_prob += prob
        if random_num < cum_prob:
            return value

from collections import Counter
results = Counter()
total = 10000
for i in xrange(total):
    results[random_variable({'A': 0.5, 'B': 0.1, 'C': 0.4})] += 1
for key, value in results.iteritems():
    print key, float(value) / total