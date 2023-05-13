# [09 세 수의 합]


# 내가 푼 것
# itertools 사용한 것 - 시간초과
from itertools import combinations
def F(nums):
  arr = list(combinations(nums, 3))
  res = []
  for c in arr:
    if sum(c) == 0:
      tmp = sorted(list(c))
      if tmp not in res:
        res.append(tmp)
  return res



# 니트코드, 책

# 세 수 a, b, c 에서
# a = 기준, b & c = 투포인터 


def F(nums):
  nums.sort()
  res = []
  for i, a in enumerate(nums):
    if i > 0 and a == nums[i-1]: # 중복 숫자 스킵
      continue
    
    l, r = i+1, len(nums)-1
    while l < r:
      sum = a + nums[l] + nums[r]
      if sum > 0:
        r -= 1
      elif sum < 0:
        l += 1
      else:
        res.append([a, nums[l], nums[r]])
        # 여기서 막힘!! 정답 처리 후 포인터 이동 방법
        # 새로운 숫자로 이동 (=중복 숫자 스킵하여 l 이동)
        # (l, r 둘 다 이동해도 됨)

        l += 1
        while nums[l] == nums[l-1] and l < r:
          l += 1
  return res


# [-4, -1, -1, 0, 1, 2]에서
# a = -1에서 [-1,0,1] 찾은 뒤, [-1,-1,2] 찾으려면
# a = -1은 고정된 상태에서 b,c (l,r포인터)를 움직어야함
