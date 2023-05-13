# [34 순열]

# 내가 푼 것

def F(nums):
  def dfs(idx, digits):
    if len(digits) == len(nums):
      result.append(digits)
      return
    for x in nums:
      if x not in digits:
        dfs(idx + 1, digits+[x])

  result = []
  dfs(0, [])
  return result



# 책 풀이 좀 어려움.
# dfs재귀 종료까지 갈 때 까지 prev에 누적됨. 그 순서가 중요.

def F(nums):
  result = []
  prev = []

  def dfs(digits):
    if len(digits) == 0:
      result.append(prev[:])
    for x in digits:
      next = digits[:]
      next.remove(x)

      prev.append(x)
      dfs(next)
      prev.pop()
  dfs(nums)
  return result