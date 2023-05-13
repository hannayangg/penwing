# [5. leetcode 53]


def F(nums):
  res = [nums[0]]
  for i in range(1, len(nums)):
    res.append(max(nums[i], res[i-1]+nums[i]))
  return max(res)


# 개선

def F(nums):
  maxSub = nums[0]
  curSum = 0
  for n in nums:
    if curSum < 0: # 갱신
      curSum = 0
    curSum += n
    maxSub = max(maxSub, curSum)    
  return maxSub