# [45. leetcode 73]



# set

def F(nums):
  s1 = set()
  s2 = set()
  for i in range(len(nums)):
    for j in range(len(nums[0])):
      if nums[i][j] == 0:
        s1.add(i)
        s2.add(j)
  
  for i in s1:
    nums[i] = [0] * len(nums[0])

  for i in range(len(nums)):
    for j in s2:
      nums[i][j] = 0



# 메모리 없이 하는 방법 - 0행, 0열에 저장

def F(nums):
  m, n = len(nums), len(nums[0])
  first_col = False
  first_row = False

  # 저장
  for i in range(m):
    for j in range(n):
      if nums[i][j] == 0:
        if i > 0: nums[i][0] = 0
        else: first_row = True
        if j > 0: nums[0][j] = 0
        else: first_col = True

  # 0으로 바꾸기
  for i in range(1, m):
    for j in range(1, n):
      if nums[i][0] == 0 or nums[0][j] == 0:
        nums[i][j] = 0

  if first_col:
    for i in range(m):
      nums[i][0] = 0

  if first_row:
    for j in range(n):
      nums[0][j] = 0
