# [77 가장 긴 반복 문자 대체]

# 부르트포스 시간 초과
# 니트코드 참고한 것 통과!!

# 조건 만족하면 사이즈 늘리고, 불만족하면 줄임.
# VALID = 바꿀 개수 <= k. (windowLen-count[흔한거] <= k)

def F(s, k):
  count = {}
  l, r = 0, 0
  res = 0
  while r < len(s):
    count[s[r]] = 1 + count.get(s[r], 0)

    # 해쉬맵 최댓값 확인
    tmp = 0
    common = ''
    for c in count:
      if count[c] > tmp:
        tmp = count[c]
        common = c

    # VALID 조건 확인, result 업데이트
    windowLen = (r-l+1)
    if windowLen - count[common] <= k:
      res = max(res, windowLen)
      r += 1
    else:
      count[s[l]] -= 1
      l += 1
      r += 1

  return res


# 개선: 니트코드
# 해쉬맵 최댓값 = max(count.values())

def F(s, k):
  count = {}
  res = 0
  l = 0
  for r in range(len(s)):
    count[s[r]] = 1 + count.get(s[r], 0)
    
    # VALID 조건 확인
    while (r-l+1) - max(count.values()) > k:
      count[s[l]] -= 1
      l += 1

    # result 업데이트
    res = max(res, r-l+1)

  return res
