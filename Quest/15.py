# [15. leetcode 70]


# Bottom up

def F(n):
  dp = [0,1,2]
  for i in range(3, n+1):
    dp.append(dp[i-1] + dp[i-2])
  return dp[n]


# dp저장공간 없이 풀기.

def F(n):
  one, two = 1, 1
  for _ in range(n-1):
    tmp = one
    one, two = two, tmp+two
    one, two
  return two