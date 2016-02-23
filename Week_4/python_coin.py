coins = [1, 5, 10, 25]

def find_change(coins, number):
    num_coins = 0
    for coin in sorted(coins, reverse=True):
        num_coins += number / coin
        number -= coin * (number / coin)
        if number % coin == 0:
            return num_coins


print find_change(coins, 100)

print find_change(coins, 74)