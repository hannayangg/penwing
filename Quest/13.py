# [13. leetcode 268]


# Sum: Sum(0~n) - Sum(nums)
def F(nums):
  n = len(nums)
  return (n*(n+1))//2 - sum(nums)


# XOR: 5^5 = 0, 5^5^3 = 3.
def F(nums):
  res = 0
  for n in nums:
    res ^= n
  for i in range(len(nums)+1):
    res ^= i
  return res  


# Sum: Sum(0~n) - Sum(nums)
def F(nums):
  n = len(nums)
  Sum = [i for i in range(n+1)]
  return sum(Sum) - sum(nums)

# Sum: 리스트 없이 풀기.
def F(nums):
  n = len(nums)
  for i in range(n):
    n += i - nums[i]
  return n