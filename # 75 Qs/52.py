# [52. leetcode 49]



import collections
def F(strs):
  hash = collections.defaultdict(list)
  for s in strs:
    hash[''.join(sorted(s))].append(s)
  return hash.values()