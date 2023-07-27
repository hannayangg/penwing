# [8. leetcode 33]

# 내가 푼 것
def F(nums, t):
  l, r = 0, len(nums)-1
  res = -1
  while l <= r:
    m = (l+r)//2
    if t == nums[m]:
      res = m
      break
    # left-sorted portion에 있는 경우
    if nums[l] <= nums[m]:
      if t > nums[m]: l = m+1
      elif t < nums[l]: l = m+1
      else: r = m-1
    # right-sorted portion에 있는 경우
    else:
      if t < nums[m]: r = m-1
      elif nums[r] < t: r = m-1
      else: l = m+1
  return res