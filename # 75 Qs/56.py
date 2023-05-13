# [56. leetcode 647]


# BF
def F(s):
  res = 0
  for i in range(len(s)):
    for j in range(i, len(s)):
      if s[i:j+1] == s[i:j+1][::-1]:
        res += 1
  return res



def F(s):
  res = 0
  for i in range(len(s)):
    # 홀수
    l = r = i
    while l >= 0 and r < len(s) and s[l]==s[r]:
      res += 1
      l -= 1
      r += 1
    # 짝수
    l, r = i, i+1
    while l >= 0 and r < len(s) and s[l]==s[r]:
      res += 1
      l -= 1
      r += 1
  return res