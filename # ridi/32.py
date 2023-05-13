# [33 섬의 개수]

# 책 풀이
# dfs(i, j): 육지를 0으로 바꾸고, 동서남북 재귀호출.
# (-> 연결된 동서남북 육지 부분도 0으로 바꾸려는 것)

def F(grid):
  def dfs(i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
      return # 바다면 종료해버림. 연결된육지만 0으로 바꿀거임.
    grid[i][j] = 0
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)
  count = 0


  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == '1':
        dfs(i, j)
        count += 1
  return count