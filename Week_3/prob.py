import numpy as np

# 1. Mathematical solution
# It is a geometric series of .5. Given, that it is 2n-1, it is 2n sig(.5) - 1. The value of a geometric series is starting value / 1 - r, or 1 / (1-.5) or 2. Applying that to the original function makes 2 * 2 - 1 or 3.


# 2. Programatic solution
def coin_flips():
    count = 1
    while np.random.randint(0, 2) != 1:
        count += 1
    return (2 * count) - 1

x = 0
sum_win = 0
while x < 100000:
    sum_win += coin_flips()
    x += 1
print sum_win/100000.