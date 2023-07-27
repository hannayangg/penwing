# [6. leetcode 152]



# n음수일 경우 max = max(min*n, n)

def F(nums):
  m = nums[0]
  n = nums[0]
  res = nums[0]
  for i in range(1, len(nums)):
    if nums[i] < 0:
      m, n = min(n*nums[i], nums[i]), max(m*nums[i], nums[i])
    else:
      m, n = min(m*nums[i], nums[i]), max(n*nums[i], nums[i])
    res = max(res, m, n)
  
  return res








# n마다 최소 최대 업데이트.
# Min*n, Max*n, n자체를 비교하여 업데이트.

def F(nums):
  res = max(nums) # 0이면 안됨: nums = [-1]
  Min, Max = 1, 1
  for n in nums:
    if n == 0:
      Min, Max = 1, 1
      continue
    tmp = Min
    Min = min(n, Min*n, Max*n)
    Max = max(n, tmp*n, Max*n)
    res = max(res, Max)
  return res