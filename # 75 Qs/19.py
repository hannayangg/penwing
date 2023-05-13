# [19. leetcode 139]


def F(s, wordDict):
  dp = [False] * (len(s)+1)
  dp[-1] = True

  for i in range(len(s)-1,-1,-1):
    for w in wordDict:
      if s[i:i+len(w)] == w:
        dp[i] = dp[i+len(w)]
      if dp[i]: break
  
  return dp[0]


# s = "aaaaaaa" wordDict = ["aaaa","aaa"]
# break 조건이 필요한 경우.