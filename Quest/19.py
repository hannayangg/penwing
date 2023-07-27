# [19. leetcode 139]


def F(s, wordDict):
  dp = [False] * (len(s)+1)
  dp[-1] = True

  for i in range(len(s)-1,-1,-1):
    for w in wordDict:
      if s[i:i+len(w)] == w:
        dp[i] = dp[i+len(w)]
      # break 바로 하면 안됨.
      # dp[i] = F일때 말고, T일 때만 break해야하기 때문.
      if dp[i]:
        break
  
  return dp[0]