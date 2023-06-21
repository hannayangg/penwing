# [29. leetcode 200]



# dfs: 1을 0으로 만들고 상하좌우 dfs.

def F(grid):
  def dfs(i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=="0":
      return
    grid[i][j] = "0"
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j-1)
    dfs(i, j+1)
  count = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == "1":
        count += 1
        dfs(i,j)
  return count


  