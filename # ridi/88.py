# [88 집 도둑]

# 내가 푼 것

def F(nums):
  if len(nums) <= 2: return max(nums)
  nums[2] += nums[0]

  for i in range(3, len(nums)):
    nums[i] += max(nums[i-2], nums[i-3])
  return max(nums)


# 책 풀이
# 내값 + 전전값 vs 전값

def F(nums):
  if len(nums) <= 2: return max(nums)
  nums[1] = max(nums[0], nums[1])

  for i in range(2, len(nums)):
    nums[i] = max(nums[i-1], nums[i-2]+nums[i])
  return nums[-1]