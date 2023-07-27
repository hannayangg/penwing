# [23. leetcode 91]


# dp[i] = dp[i+1] + dp[i+2]

def S(s):
  dp = [None] * len(s)
  def F(i):
    if i > len(s): return 0
    if i == len(s): return 1
    if dp[i]: return dp[i]

    res = 0
    if int(s[i]) > 0:
      res += F(i+1)
    if s[i] != '0' and int(s[i:i+2]) <= 26:
      res += F(i+2)

    dp[i] = res
    return res
  return F(0)


def F(s):
  dp = [0] * (len(s) + 2)
  dp[-2] = 1
  dp[-1] = 0
  for i in range(len(s)-1, -1, -1):
    if int(s[i]) > 0:
      dp[i] += dp[i+1]
    if s[i] != '0' and int(s[i:i+2]) <= 26:
      dp[i] += dp[i+2]
  return dp[0]





# 개선 - 해쉬맵 / s[i] == '0'일 때를 먼저 처리.

def S(s):
  dp = {len(s): 1}
  def F(i):
    if i in dp: return dp[i]
    if s[i] == '0': return 0 ###

    res = F(i+1) # 한자리 무조건 됨.
    if 10 <= int(s[i:i+2]) <= 26:
      res += F(i+2)

    dp[i] = res
    return res

  return F(0)




def F(s):
  dp = {len(s): 1}

  for i in range(len(s)-1, -1, -1):
    if s[i] == '0': ###
      dp[i] = 0
    else:
      dp[i] = dp[i+1]
    if 10 <= int(s[i:i+2]) <= 26:
      dp[i] += dp[i+2]

  return dp[0]