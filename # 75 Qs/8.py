# [8. leetcode 33]



# 이분탐색 해보려 했지만 조건 찾는걸 못하겠음
def F(nums, t):
  if t not in nums: return -1
  return nums.index(t)



# [4,5,6,7,0,1,2] 에서 
# mid 6일 때, mid 1일 때를 나눠서 생각해보기.

def F(nums, t):
  l, r = 0, len(nums)-1
  while l <= r:
    m = (l+r)//2
    if nums[m] == t:
      print(m)
      break
    
    # m이 left sorted portion에 속한 경우
    if nums[l] <= nums[m]:
      if (t > nums[m]) or (t < nums[l]):
        l = m+1
      else:
        r = m-1
    
    # right sorted portion
    else:
      if (t < nums[m]) or (t > nums[r]):
        r = m-1
      else:
        l = m+1
        
  return -1