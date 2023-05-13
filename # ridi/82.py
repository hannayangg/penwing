# [82 쿠키 부여]

# 내가 푼 것 - 정렬 후 투포인터
def F(child, cookie):
  child.sort()
  cookie.sort()
  l, r, res= 0, 0, 0
  while l < len(child) and r < len(cookie):
    if child[l] <= cookie[r]:
      res += 1
      l += 1
      r += 1
    else:
      r += 1
  return res

# 책풀이: res = l. res 필요없음.
