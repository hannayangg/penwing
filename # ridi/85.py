# [85 피보나치 수열]

# 내가 푼 것

def F(n):
  dp = [0, 1]
  for i in range(2, n+1):
    new = dp[i-1] + dp[i-2]
    dp.append(new)
  return dp[n]

dp = {0: 0, 1: 1}
def F(n):
  if n in dp:
    return dp[n]
  dp[n] = F(n-1) + F(n-2)
  return dp[n]