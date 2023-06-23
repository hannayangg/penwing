# [27. leetcode 207]


def _F(numCourses, prerequisites):
  dp = [[] for _  in range(numCourses)]
  for crs, pre in prerequisites:
    dp[crs].append(pre)

  def dfs(crs):
    if dp[crs] is None: return True
    if crs in visit: return False
    visit.add(crs)
    for pre in dp[crs]:
      if not dfs(pre): return False
    visit.remove(crs) # 중요   
    dp[crs] = [] # 중요
    # True코스를 비우면, 재방문시 바로 True 리턴.
    return True

  visit = set()
  for crs in range(numCourses):
    if not dfs(crs):
      return False
  return True



# visit.remove()가 필요한 예: [[0,1],[0,2],[1,3]]
# 재귀는 종료를 만날때까지 안으로 들어간다.

# dfs(0, {}) -> dfs(1, {0}) -> dfs(3, {0,"1"}) -> True로 종료.
# 그 다음에야 dfs(2, {0}) 를 진행하게 되는데,
# 만약 remove조건이 없다면, dfs(2, {0,"1"}) 로 진행되게 된다. 