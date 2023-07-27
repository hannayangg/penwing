# [3. leetcode 217]



# 내가 푼 것 - Counter, 셋

import collections
def F(nums):
  if collections.Counter(nums).most_common()[0][1] > 1:
    return True
  return False

def F(nums):
  return len(set(nums)) < len(nums)

def F(nums):
  seen = set()
  for n in nums:
    if n in seen:
      return True
    seen.add(n)
  return False