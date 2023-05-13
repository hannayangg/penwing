# [31 상위 k 빈도요소]

# 내가 푼 것 - Counter.most_common() 이용

import collections

def F(nums, k):
  h = collections.Counter(nums).most_common(k)
  res = []
  for c in h:
    res.append(c[0])
  return res

# 개선: list(zip(*collections.Counter(nums).most_common(k)))[0]


# zip 과 * (언패킹) 이용
# [(1,2), (2,3), (3,5)] -> k=3일 때 [(1,2,3), (2,3,5)]
# (key, value)에서 key들만 묶어서 list[0]에 저장됨.