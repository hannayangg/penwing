# [87 계단 오르기]

# 내가 푼 것 - 피보나치랑 같음
def F(n):  
  dp = [1,1]
  for i in range(2, n+1):
      dp.append(dp[i-1] + dp[i-2])
  return dp[n]