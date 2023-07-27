# [16. leetcode 322]


# bottom up. 앞값 + 1.

def F(coins, amount):
  dp = [float("inf")] * (amount+1)
  dp[0] = 0
  
  # dp[i] = dp[i-n] + 1
  for i in range(1, amount+1):
    for n in coins:
      if i-n >= 0:
        dp[i] = min(dp[i], dp[i-n]+1)

  return dp[amount] if dp[amount] != float("inf") else -1