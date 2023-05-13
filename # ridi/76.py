# [76 부분문자열]

# 딕셔너리
count = {}
t = 'abc'
for c in t:
  count[c] = 1 + count.get(c, 0) # c값, 없다면 0

count.get('a', 0) # 'a'값, 없다면 0 뱉어라  
count.get('d', 0) # 'd'값, 없다면 0 뱉어라 => 0!



# 니트코드. 복잡.
# have(초기값 0) == need(t 개수) 만족하면 result 업데이트.

def F(s, t):
  window, countT = {}, {}
  for c in t:
    countT[c] = 1 + countT.get(c, 0)
  have, need = 0, len(countT)
  res, resLen = [-1, -1], float("infinity")
  

  l = 0
  for r in range(len(s)):
    c = s[r]
    window[c] = 1 + window.get(c, 0)

    if c in countT and countT[c] == window[c]:
      have += 1
    

    while have == need:
      # result 업데이트
      if (r-l+1) < resLen:
        res = [l, r]
        resLen = (r-l+1)
      
      # l움직여 윈도우 사이즈 줄이기
      window[s[l]] -= 1
      if s[l] in countT and window[s[l]] < countT[s[l]]:
        have -= 1
      l += 1

  l, r = res
  return s[l:r+1] if res is not float("infinity") else ""