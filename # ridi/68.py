# [68 두 수의 합2]

# 내가 푼 것
# 투포인터, 빠름.
def F(nums, target):
  l, r = 0, len(nums)-1
  while l < r:
    if nums[l] + nums[r] < target:
      l += 1
    elif nums[l] + nums[r] > target:
      r -= 1
    else:
      return [l+1, r+1]

# 이진탐색, 엄청 느림.
import bisect
def F(nums, target):
  for i, v in enumerate(nums):
    c = target - v
    c_idx = bisect.bisect_left(nums[i+1:], c) + (i+1)
    if c_idx < len(nums) and nums[c_idx] == c:
      return [i+1, c_idx+1]


# 개선: bisect모듈 사용
# bisect.bisect_left(리스트, 찾는값, 범위제힌!!)
def F(nums, target):
  for i, v in enumerate(nums):
    c = target - v
    c_idx = bisect.bisect_left(nums, c, i+1)
    if c_idx < len(nums) and nums[c_idx] == c:
      return [i+1, c_idx+1]