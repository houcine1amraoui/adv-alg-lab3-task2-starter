def brute_force(coins, amount):
    # Base cases
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')  # invalid path
    
    # Try each coin
    min_coins = float('inf')

    for coin in coins:
        res = brute_force(coins, amount - coin)
        if res != float('inf'):
            min_coins = min(min_coins, 1 + res)

    return min_coins

def dynamic_programming(coins, amount, memo=None):
    # modify the brute force function
    # with memoization

    # Base cases
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf') # invalid path

    # Try each coin
    min_coins = float('inf')

    for coin in coins:
        res = dynamic_programming(coins, amount - coin, memo)
        if res != float('inf'):
            min_coins = min(min_coins, 1 + res)

    return min_coins