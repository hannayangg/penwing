# [36. leetcode 435]

def F(arr):
  arr.sort()
  res = 0
  pre = arr[0][1]
  for i in range(1, len(arr)):
    l, r = arr[i]
    if pre > l:
      res += 1
      pre = min(pre, r)
    else:
      pre = r
  return res