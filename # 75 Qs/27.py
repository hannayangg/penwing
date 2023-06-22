# [27. leetcode 207]


# dfs(i) T: dp[i]==[] / F: loop(set 필요)

def _F(numCourses, prerequisites):
  dp = [[] for _  in range(numCourses)]
  for crs, pre in prerequisites:
    dp[crs].append(pre)

  def dfs(crs):
    if dp[crs] is None: return True
    if crs in been: return False
    been.add(crs)
    for pre in dp[crs]:
      if not dfs(pre):
        return False
    been.remove(crs)
    
    dp[crs] = [] # 시간 초과하지 않으려면 필요한 구절!
    # True인 코스는 빈 리스트로 만들어야,
    # 다음에 방문했을 때 바로 True 리턴 가능
    return True

  been = set()
  for crs in range(numCourses):
    if not dfs(crs):
      return False
  return True