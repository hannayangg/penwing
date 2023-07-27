# [4. leetcode 238]



# 내가 푼 것

def F(nums):
  res = [1] * len(nums)
  
  # 자신 앞 누적곱을 넘겨받음
  n = 1
  for i in range(len(res)):
    res[i] *= n
    n *= nums[i]

  # 자신 뒤 누적곱을 넘겨받음
  n = 1
  for i in range(len(res)-1, -1, -1):
    res[i] *= n
    n *= nums[i]
  
  return res