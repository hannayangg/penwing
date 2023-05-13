# [18. leetcode 1143]

# TopDown: 시간 초과

def F(t1, t2):
  if not t1 or not t2: return 0
  if t1[0] == t2[0]: return F(t1[1:], t2[1:]) + 1
  else:
    tmp1, tmp2 = t1, t2
    return max(F(t1, t2[1:]), F(tmp1[1:], tmp2))




# BottomUp: dp 2차원으로 만들 때, ij 설정 주의19.

def F(t1, t2):
  dp = [[0 for j in range(len(t2)+1)] for i in range(len(t1)+1)]
  
  for i in range(len(t1)-1, -1, -1):
    for j in range(len(t2)-1, -1, -1):
      if t1[i] == t2[j]:
        dp[i][j] = dp[i+1][j+1] + 1
      else:
        dp[i][j] = max(dp[i+1][j], dp[i][j+1])
  
  return dp[0][0]