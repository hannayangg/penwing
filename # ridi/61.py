# [61 가장 큰 수]

# 내가 푼 것 개선
# 1. 숫자 리스트를 문자열로: list(map(str,nums)).
# 2. 애초에 큰 순서로 정렬.
# 3. '00'방지: str(int()).

def F(nums):
  nums = list(map(str, nums))

  for i in range(1, len(nums)):
    key = nums[i]
    j = i-1
    while j >= 0 and nums[j] + key < key + nums[j]:
      nums[j+1] = nums[j]
      j -= 1
    nums[j+1] = key

  return str(int(''.join(nums)))



# 책 풀이
# 삽입정렬 코드가 좀 다름!!!

def F(nums):
  i = 1
  while i < len(nums):
    j = i
    while j > 0 and nums[j-1] > nums[j]:
      nums[j], nums[j-1] = nums[j-1], nums[j]
      j -= 1
    i += 1
  return nums
