# [24. leetcode 62]




# dp[i][j] = dp[i+1][j] + dp[i][j+1]



def F(m, n):
  dp = [[0 for j in range(n+1)] for i in range(m+1)]
  for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
      if i == m-1 and j == n-1:
        dp[i][j] = 1
        continue
      dp[i][j] = dp[i+1][j] + dp[i][j+1]
 
  return dp[0][0]