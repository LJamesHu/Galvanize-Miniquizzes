import random
import numpy as np


def random_element(stream, k=1):
    samples = np.zeros(k)
    for i, val in enumerate(stream):
        for index in xrange(k):
            if random.random() < 1/(i+1.):
                samples[index] = val
    return samples

print random_element([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print random_element([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10000)