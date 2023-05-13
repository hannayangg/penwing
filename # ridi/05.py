# [05 그룹 애너그램]





# 내가 푼 것
# sorted('eat') => ['a','e','t'] 리스트 안씌워도 됨.

import collections
def group(strs):
  h = collections.defaultdict(list)
  for x in strs:
    h[''.join(sorted(x))].append(x)
  return list(h.values())

