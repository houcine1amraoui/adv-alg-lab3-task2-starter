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

def memoization(coins, amount, memo=None):
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
        res = memoization(coins, amount - coin, memo)
        if res != float('inf'):
            min_coins = min(min_coins, 1 + res)

    return min_coins

def bottom_up(coins, amount):
    # Create DP table of size amount+1
    # dp[x] = minimum coins needed to make amount x
    dp = [float('inf')] * (amount + 1)

    # Base case: 0 coins needed to make amount 0
    dp[0] = 0

    # complete the code
    
