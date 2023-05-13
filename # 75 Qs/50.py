# [50. leetcode 424]




# 니트코드

def F(s, k):
  count = {}
  res = 0
  l = 0
  
  for r in range(len(s)):
    count[s[r]] = 1 + count.get(s[r], 0)
    # invalid
    while (r-l+1) - max(count.values()) > k:
      count[s[l]] -= 1
      l += 1
    res = max(res, r-l+1)
  return res




# valid: windowLen - maxF <= k

import collections
def F(s, k):
  count = collections.defaultdict(int)
  res = 0
  l = 0

  for r in range(len(s)):
    count[s[r]] += 1
    # valid
    if (r-l+1) - max(count.values()) <= k:
      res = max(res, r-l+1)
    # invalid
    else:
      count[s[l]]-=1
      l += 1
  return res