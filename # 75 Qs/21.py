# [21. leetcode 198]

def F(nums):
  for i in range(2, len(nums)):
    if i == 2:
      nums[i] += nums[0]
      continue
    nums[i] += max(nums[i-2], nums[i-3])
  return max(nums)




# nums 변화 없는 풀이.
# rob1과 rob2변수에 값들을 저장.

def F(nums):
  rob1, rob2 = 0, 0
  for n in nums:
    tmp = max(rob1+n, rob2)
    # rob1, rob2 업데이트!!
    rob1 = rob2
    rob2 = tmp
  return rob2