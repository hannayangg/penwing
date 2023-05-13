# [06 팰린드롬]

# 내가 푼 것 - 메모 봄.
def F(s):
  res = ''
  resLen = 1
  
  # 팰린드롬이 홀수일때
  for i in range(len(s)):
    l, r = i-1, i+1
    while l >= 0 and r < len(s) and s[l] == s[r]:
      l -= 1
      r += 1
    if resLen < r-l:
      resLen = r-l
      res = s[l+1:r]

  # 짝수일 때
  for i in range(len(s)):
    l, r = i, i+1
    while l >= 0 and r < len(s) and s[l] == s[r]:
      l -= 1
      r += 1
    if resLen < r-l:
      resLen = r-l
      res = s[l+1:r]
  
  return res



# 책 - 내부 함수로 더 간단함.
def F(s):
  def expand(l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
      l -= 1
      r += 1
    return s[l+1:r]

  if len(s) < 2 or s == s[::-1]: return s
  res = '' 
  for i in range(len(s)-1):
    res = max(res, expand(i, i+1), expand(i, i+2), key = len)
    # 짝수일 때, 홀수일 때

  return res