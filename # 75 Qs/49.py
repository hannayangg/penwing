# [49. leetcode 3]


# 중복 있다면 윈도우사이즈 줄이기 (l += 1).
def F(s):
  l = r = 0
  res = 0
  while r < len(s):
    # 중복 없음
    if s[r] not in s[l:r]:
      res = max(res, r-l+1)
      r += 1
    # 중복 있음
    else: l += 1
  return res


# 중복 체크 set 이용.
def F(s):
  charSet = set()
  l = 0
  res = 0
  for r in range(len(s)):
    # 중복 있음
    while s[r] in charSet:
      charSet.remove(s[l])
      l += 1
    charSet.add(s[r])
    res = max(res, r-l+1)
  return res