# [9. leetcode 15]


# 내가 푼 것: r 중복만 스킵.
# l,r 모두 중복 스킵하는 방법 모름.




def F(nums):
  nums.sort()
  res = []

  for a in range(len(nums)-1):
    # 양수/중복스킵
    if (nums[a] > 0) or (a > 0 and nums[a] == nums[a-1]):
      continue
    
    b, c = a+1, len(nums)-1
    while b < c:

      # c 중복스킵
      if c < len(nums)-1 and nums[c] == nums[c+1]:
        c -= 1
        continue

      # b 중복스킵 (*b가 출발시점에 있을 때는 스킵제외)
      if b > a+1 and nums[b] == nums[b-1]:
        b += 1
        continue

      # 투포인터
      curSum = nums[a]+nums[b]+nums[c]
      if curSum == 0:
        res.append([nums[a], nums[b], nums[c]])
        b += 1
        c -= 1
      elif curSum < 0:
        b += 1
      else:
        c -= 1
  return res