# [22. leetcode 213]




# 21번문제 활용
def F(nums):
  if len(nums) == 1:
    return nums[0]

  rob1, rob2 = 0, 0
  p = nums.pop()
  for n in nums:
    tmp = max(rob1+n, rob2)
    rob1 = rob2
    rob2 = tmp
  
  rob3, rob4 = 0, 0
  nums.append(p)
  nums.pop(0)
  for n in nums:
    tmp = max(rob3+n, rob4)
    rob3 = rob4
    rob4 = tmp

  return max(rob2, rob4)




# 내부함수.
def S(nums):
  
  def F(nums):
    rob1, rob2 = 0, 0
    for n in nums:
      tmp = max(rob1+n, rob2)
      rob1 = rob2
      rob2 = tmp
    return rob2
  
  return max(nums[0], F(nums[1:]), F(nums[:-1]))