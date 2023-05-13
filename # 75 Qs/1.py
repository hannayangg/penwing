# [1. leetcode 1]



# 내가 푼 것 - 해쉬맵

def F(nums, target):
  hash = {}
  for i, v in enumerate(nums):
    com = target - v
    if com in hash:
      return [hash[com], i]
    hash[v] = i



# nums의 n의 [이전 포션]만 hash에 저장된다.