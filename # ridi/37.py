# [37 부분집합]

# 내가 푼 것

def F(nums):
  def dfs(lev, path):
    if lev == len(nums):
      result.append(path)
      return
    dfs(lev+1, path+[nums[lev]])
    dfs(lev+1, path)
  result = []
  dfs(0, [])
  return result


# 책 풀이
# 함수 실행 되자마자 path를 저장하고, idx, path 늘린 dfs 재귀호출
# 재귀함수 호출 하자마자 result에 누적하는 게 특징적임.

def F(nums):
  def dfs(idx, path):
    result.append(path)
    for i in range(idx, len(nums)):
      dfs(i+1, path+[nums[i]])
  result = []
  dfs(0, [])
  return result