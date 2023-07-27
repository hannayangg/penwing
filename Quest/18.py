# [18. leetcode 1143]


# dp 2차원.

def F(t1, t2):
  dp = [[0 for j in range(len(t2)+1)] for i in range(len(t1)+1)]
  # dp = [[0]*(len(t2)+1)]*(len(t1)+1) 로 하면 안되.
  # 이렇게 할 경우, 값 바뀔 때 다른 값도 바뀌어버림.

  for i in range(len(t1)-1, -1, -1):
    for j in range(len(t2)-1, -1, -1):
      if t1[i] == t2[j]:
        dp[i][j] = 1 + dp[i+1][j+1]
      else:
        dp[i][j] = max(dp[i+1][j], dp[i][j+1])
  
  return dp[0][0]
