"""
Problem 30:

In England the currency is made up of pound, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, 100p and 200p.

It is possible to make 200p in the following way:

    1x100p + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can 200p be made using any number of coins?
"""
def n_combos(target_sum, coins):
    total_count = 0
    current_coin = coins[0]
    if len(coins) == 1:
        return 1 if total_count % current_coin == 0 else 0
    for i in range(target_sum // current_coin + 1):
        total_count += n_combos(target_sum - i * current_coin, coins[1:])
    return total_count

def main():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    target_sum = 200
    print(n_combos(target_sum, coins))

if __name__ == "__main__":
    main()
