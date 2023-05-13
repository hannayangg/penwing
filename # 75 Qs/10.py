# [10. leetcode 11]


# 투포인터.

def F(nums):
  l, r = 0, len(nums)-1
  res = 0
  while l < r:
    res = max(res, (r-l)*(min(nums[l], nums[r])))
    if nums[l] <= nums[r]:
      l += 1
    else:
      r -= 1
  return res


def F(nums):
  l, r = 0, len(nums)-1
  res = 0
  while l < r:
    if nums[l] <= nums[r]:
      res = max(res, (r-l)*nums[l])
      l += 1
    else:
      res = max(res, (r-l)*nums[r])
      r -= 1
  return res