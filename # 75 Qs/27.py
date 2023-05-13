# [27. leetcode 207]


# dfs(i) T: dp[i]==[] / F: loop(set 필요)

def F(n, pre):
  dp = [[] for _ in range(n)]
  for v0, v1 in pre:
    dp[v0].append(v1)
  been = set()
  def dfs(i):
    if dp[i] == []: return True
    if i in been: return False
    been.add(i)
    for j in dp[i]:
      if not dfs(j): return False
    been.remove(i)
    dp[i] = []
    return True
  
  for i in range(n):
    if not dfs(i): return False
  return True



# 주의! T일 경우, set에서 i 삭제.
# n = 5, pre = [[0,1],[0,3],[1,2],[3,2]]
# 주의! 모든 i를 돌림.(코스들 분리된 경우)
# n = 4, pre = [[0,1],[2,3],[3,2]]