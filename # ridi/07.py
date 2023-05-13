# [07 두 수의 합]



# 내가 푼 것
# hash에 n추가를 마지막에 하기에,
# n입장에서 hash에는 이전 값들만 저장되어 있음.

def F(nums, target):
  hash = {}
  for i, v in enumerate(nums):
    com = target - v
    if com in hash:
      return [hash[com], i]
    hash[v] = i
