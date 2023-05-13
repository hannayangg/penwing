# [01 유효한 팰린드롬]

# 내가 푼 것

def F(s):
  s = re.sub('[^a-z0-9]', '', s.lower())
  return s == s[::-1]

import re
def F(s):
  s = re.sub('[^a-z0-9]', '', s.lower())
  l, r = 0, len(s)-1
  while l < r:
    if s[l] != s[r]:
      return False
    l += 1
    r -= 1
  return True


# 특수문자 제거 방법
# re.sub('[^a-z0-9]', '', s)
# x.isalnum()