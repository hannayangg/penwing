# [21. leetcode 198]


# 1단계
def F(nums):
  for i in range(2, len(nums)):
    if i == 2:
      nums[2]+=nums[0]
      continue
    nums[i] += max(nums[i-2], nums[i-3])
  return max(nums)






# 2단계: 현재값 = max(전값, 현재값+전전값)
def F(nums):
    if len(nums)==1: return nums[0]
    nums[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        nums[i] = max(nums[i-1], nums[i]+nums[i-2])
    return nums[-1]





# 3단계: 전값, 전전값을 변수로.
# [rob1, rob2, n, ...]


def F(nums):
  rob1, rob2 = 0, 0
  for n in nums:
    tmp = max(rob1+n, rob2)
    rob1 = rob2
    rob2 = tmp
  return rob2