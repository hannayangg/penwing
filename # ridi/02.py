# [02 문자열 뒤집기]

# 내가 푼 것 - 투포인터

def F(s):
  l, r = 0, len(s)-1
  while l < r:
    s[l], s[r] = s[r], s[l]
    l += 1
    r -= 1