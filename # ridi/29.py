# [29 보석과 돌]

# 내가 푼 것

import collections

def F(J, S):
  h = collections.Counter(S)
  res = 0

  for x in J: # 개선: 비교 생략 가능
    if x in h:
      res += h[x]
  return res

  # defaultdict, Counter -> 비교 생략 가능함
  # for x in J: count += h[x]