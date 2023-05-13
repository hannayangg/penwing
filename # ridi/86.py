# [86 최대 서브 배열]

import sys
# 내가 푼 것
def F(nums):
  curSum = 0
  res = -sys.maxsize
  for n in nums:
      curSum += n
      res = max(res, curSum)
      if curSum < 0:
          curSum = 0
  return res
# 실패한 방법: 해쉬맵에 모든 값 저장. (저장공간 초과)
# 투포인터. (l,r이 중앙으로 모여들어서 안됨)


# 책풀이
# 상향식. 이전값 누적해나가기.
# 이전 값이 음수일 경우 0 누적. (버림)

def F(nums):
  for i in range(1, len(nums)):
    nums[i] += nums[i-1] if nums[i-1] > 0 else 0
  return nums