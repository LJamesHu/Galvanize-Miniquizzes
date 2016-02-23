import numpy as np


# o    o
# 8b   8
# 8`b  8 o    o ooYoYo. .oPYo. o    o
# 8 `b 8 8    8 8' 8  8 8    8 8    8
# 8  `b8 8    8 8  8  8 8    8 8    8
# 8   `8 `YooP' 8  8  8 8YooP' `YooP8
# ..:::..:.....:..:..:..8 ....::....8
# ::::::::::::::::::::::8 :::::::ooP'.
# ::::::::::::::::::::::..:::::::...::
# 1. Closest non numpy
def closest(array, value):
    return array[min(range(len(array)), key=lambda i: abs(array[i] - value))]

print closest([10, 17, 2, 29, 16], 14)


# 2. Closest with numpy
def closest_np(array, value):
    return array[(np.abs(np.array(array) - value)).argmin()]

print closest_np([10, 17, 2, 29, 16], 14)


#3. Masking
x = np.array([[4, 3], [-1, 2], [-1, 6], [-1, 3], [-1, 2]])
y = np.array([1, -1, 1, 20, -20])

z = y > 0

print x[z]

