# [30. leetcode 128]


def F(nums):
  nums = sorted(list(set(nums)))
  res = 1
  result = 1
  for i in range(1, len(nums)):
    if nums[i] == nums[i-1] + 1:
      res += 1
      result = max(res, result)
    else:
      res = 1
  return result