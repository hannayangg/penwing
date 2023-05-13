# [30 중복문자없는 가장긴부분문자열]


# 내가 푼 것
# for i 돌면서 그 i부터의 최대 길이 저장

def F(s):
  if not s: return 0
  res = []
  for i, v in enumerate(s):
    tmp = v
    idx = i+1
    while idx < len(s) and s[idx] not in tmp:
      tmp += s[idx]
      idx += 1
    res.append(idx-i)
  return max(res)




# 니트코드
# 슬라이딩 윈도우. [for r] r을 기준으로, l포인터 찾기. 등장한 문자는 셋에 저장하여 확인.

def F(s):
  been = set()
  l = 0
  res = 0
  for r in range(len(s)):
    while s[r] in been:
      been.remove(s[l]) ###
      l += 1
    been.add(s[r])
    res = max(res, r-l+1)
  return res




# 이부분 주의!
# s[r]이 아니라 s[l]을 지움.
# s[r]이랑 같은 문자가 셋에서 사라질 때까지 l += 1 하면서 다 지움.