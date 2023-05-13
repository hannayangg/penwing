# [83 과반수 엘리먼트]

# 내가 푼 것

def F(nums):
  m = len(nums)//2
  return sorted(nums)[m]





# 책풀이
# L, R 분할 후, 둘 중 과반수 넘은 것 리턴.
# 과반수 조건: count(L) > m (절반)

def F(nums):
  if not nums: return None
  if len(nums) == 1: return nums[0]

  # L, R 분할
  m = len(nums)//2
  L = F(nums[:m])
  R = F(nums[m:])

  # L or R 리턴
  if nums.count(L) > m:
    return L
  return R







# 니트코드

def F(nums):
  res, count = 0, 0 
  for n in nums:
    if count == 0:
      res = n
    count += (1 if n == res else -1)
  return res