# [55. leetcode 5]




def F(s):
  res = ''
  resLen = 0
  # 홀수 'bab'
  for i in range(len(s)):
    l, r = i-1, i+1
    while l >= 0 and r < len(s) and s[l] == s[r]:
      l -= 1
      r += 1
    if (r-l+1) > resLen:
      resLen = r-l+1
      res = s[l+1:r]
  # 짝수 'caac'
  for i in range(len(s)):
    l, r = i, i+1
    while l >= 0 and r < len(s) and s[l] == s[r]:
      l -= 1
      r += 1
    if (r-l+1) > resLen:
      resLen = r-l+1
      res = s[l+1:r]
  return res