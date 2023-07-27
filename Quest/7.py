# [7. leetcode 153]


def F(nums):
  return min(nums)

def F(nums):
  l, r = 0, len(nums)-1
  while l <= r:
    m = (l+r)//2
    
    # 직전보다 작다면 정답
    if nums[m] <= nums[m-1]:
      return nums[m]
    
    elif nums[m] > nums[r]:
      l = m+1
    else:
      r = m-1