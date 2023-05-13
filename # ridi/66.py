# [66 회전 정렬된 배열]

# 내가 푼 것.

def F(nums, target):
  if target not in nums:
    return -1
  return nums.index(target)

# 니트코드

def F(nums, target):
  l, r = 0, len(nums)-1
  while l <= r:
    mid = (l+r)//2
    if target == nums[mid]:
      return mid
    if nums[l] <= nums[mid]:
      if target > nums[mid] or target < nums[l]:
        l = mid + 1
      else:
        r = mid - 1
    else:
      if target < nums[mid] or target > nums[r]:
        r = mid - 1
      else:
        l = mid + 1
  return -1