# [29. leetcode 200]



# 전체순회하면서 육지 만나면 개수 증가.
# 중복체크 방지를 위해 육지는 바다로 만들고, 인접육지도 모두 바다로 만들기.


def F(grid):
  def bfs(i, j):
    # 종료조건: 인덱스 범위 밖이거나 바다인 경우.
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='0': return
    # 중복체크 방지를 위해, 바다로 만들기.
    grid[i][j] = "0"
    # 인접육지가 중복체크 방지를 위해, 인접육지도 모두 바다로 만들기.
    bfs(i+1,j)
    bfs(i-1,j)
    bfs(i,j+1)
    bfs(i,j-1)

  count=0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      # 육지인 경우 최종 개수 증가.
      if grid[i][j] == '1':
        count += 1
        bfs(i, j)
  return count

  