# [16. leetcode 322]


# BottomUp: 이전값(코인 뺀 값) + 1.

def F(coins, amount):
  dp = [0]
  for i in range(1, amount+1):
    prev = []
    for n in coins:
      if i>=n:
        prev.append(dp[i-n])
    dp.append(min(prev)+1 if prev else float("inf"))
  return dp[amount]



# prev 없앤 방법.

def F(coins, amount):
  dp = [float("inf")] * (amount+1)
  dp[0] = 0
  for i in range(1, amount+1):
    
    for n in coins:
      if i-n >= 0:
        dp[i] = min(dp[i], dp[i-n]+1)

  return dp[amount] if dp[amount] != float("inf") else -1