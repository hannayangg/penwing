# [9. leetcode 15]

def F(nums):
  nums.sort()
  res = []
  for i in range(len(nums)):
    # 첫 숫자 중복 방지 [0,0,0,0]
    if i > 0 and nums[i-1] == nums[i]:
      continue
    
    l, r = i+1, len(nums)-1  
    while l < r:
      curSum = nums[i] + nums[l] + nums[r]
      if curSum < 0: l += 1
      elif curSum > 0: r -= 1

      else:
        res.append([nums[i], nums[l], nums[r]])
        l += 1
        # l 중복 방지
        while nums[l-1] == nums[l] and l < r:
          l += 1
  
  return res