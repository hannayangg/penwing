# [10. leetcode 11]


# 투포인터.
def F(nums):
  l, r = 0, len(nums)-1
  res = 0
  while l < r:
    a = r-l
    b = min(nums[l], nums[r])
    res = max(res, a*b)
    if nums[l] < nums[r]:
      l += 1
    else:
      r -= 1
  return res