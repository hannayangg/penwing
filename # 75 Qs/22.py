# [22. leetcode 213]



# nums[-1] rob하면, nums[0]은 못함.
# nums[0] rob 하면, nums[-1]은 못함.
# 두 subproblems의 max를 구하기.

def F(nums):
  rob1, rob2 = 0, 0
  for i in range(1, len(nums)):
    tmp = max(rob2, nums[i]+rob1)
    rob1 = rob2
    rob2 = tmp
  
  rob1, rob2 = 0, 0
  for i in range(len(nums)-1):
    _tmp = max(rob2, nums[i]+rob1)
    rob1 = rob2
    rob2 = _tmp

  return max(tmp, _tmp)




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