# [51. leetcode 76]



def F(s, t):
  # 목표
  need = len(t)
  map = collections.defaultdict(int)
  for char in t:
    map[char] += 1
  
  # 현재
  have = 0
  hash = collections.defaultdict(int)
  
  res, resLen = "", len(s)
  l = 0
  for r in range(len(s)):
    hash[s[r]] += 1
    if s[r] in map and map[s[r]] == hash[s[r]]:
      have += 1
    
    # VALID => l이동, 범위줄이기
    while need == have:
      if (r-l+1) <= resLen:
        res = s[l:r+1]
        resLen = r-l+1
      hash[s[l]] -= 1
      if s[l] in map and map[s[l]] > hash[s[l]]:
        have -= 1
      l += 1
  return res