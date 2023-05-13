# [70 싱글 넘버]

# 내가 푼 것 - 포인터 두 개를 비교.

def F(nums):
  nums.sort()
  l, r = 0, 1
  while r < len(nums):
    if nums[l] != nums[r]:
      return nums[l]
    l += 2
    r += 2
  return nums[-1]


# 책 풀이 - XOR
# 2^2^1 = 1. (두 수가 같으면 0)

def F(nums):
  for i in range(1, len(nums)):
    nums[0] ^= nums[i]
  return nums[0] # res = 0으로 두고 누적해도 됨.