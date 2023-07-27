# [12. leetcode 338]


def F(n):
  dp = [0]
  i = 1
  while i <= n:
    for j in range(i):
      dp.append(1 + dp[j-i])
    i *= 2
  return dp[:n+1]




# 1~16까지 2진수로 표현하여 규칙성 찾기.
# dp[n-offset] offset 1, 2, 4, 8 등비수열.

def F(n):
  dp = [0] * (n+1)

  offset = 1
  for i in range(1, n+1):
    if offset * 2 == i:
      offset = i
    dp[i] = 1 + dp[i-offset]

  return dp