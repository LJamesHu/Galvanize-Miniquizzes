# .oPYo.
# 8    8
# 8      .oPYo. odYo.
# 8   oo 8oooo8 8' `8
# 8    8 8.     8   8
# `YooP8 `Yooo' 8   8
# :....8 :.....:..::..
# :::::8 :::::::::::::
# :::::..:::::::::::::

def prime_generator():
    D = {}

    q = 2

    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

# p = prime_generator()
# print p.next()
# print p.next()
# print p.next()
# print p.next()
# print p.next()


# o     o                   .o  .oPYo.             8
# 8b   d8                  .o'  8   `8             8
# 8`b d'8 .oPYo. .oPYo.   .o'  o8YooP' .oPYo. .oPYo8 o    o .oPYo. .oPYo.
# 8 `o' 8 .oooo8 8    8  .o'    8   `b 8oooo8 8    8 8    8 8    ' 8oooo8
# 8     8 8    8 8    8 .o'     8    8 8.     8    8 8    8 8    . 8.
# 8     8 `YooP8 8YooP' o'      8    8 `Yooo' `YooP' `YooP' `YooP' `Yooo'
# ..::::..:.....:8 ....:..::::::..:::..:.....::.....::.....::.....::.....:
# :::::::::::::::8 :::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::..:::::::::::::::::::::::::::::::::::::::::::::::::::::::

import operator

sfif = "San Francisco is fun!"

def acronym(s):
    return reduce(operator.add, map(lambda x: x[0].upper(), s.split()))

print acronym(sfif)