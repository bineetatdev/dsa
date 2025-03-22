#Day8 Q2
# Given an array of coins coins[] and an integer amount, find the minimum number of coins needed to make up that amount. If it's not possible, return -1.

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)  # Initialize with infinity
    dp[0] = 0  # Base case: No coins needed for amount 0

    for coin in coins:  # Iterate over each coin
        for i in range(coin, amount + 1):  # Compute min coins for each amount
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Time Complexity: O(amount * len(coins))
# Space Complexity: O(amount) for storing the DP table
coins = [1, 2, 5]
amount = 11 

