# [28. leetcode 417]




heights = [[1,2,2,3,5],
          [3,2,3,4,4],
          [2,4,5,3,1],
          [6,7,1,4,5],
          [5,1,1,2,4]]



# 주의..
# 완전히 가로 방향으로만, 세로방향으로만 이동하는 게 아님.
# 인접해 있으면 가로로 갔다가 세로로 갈 수 있음.
# (1,3)(1,4)가 그 예시임.
# 가로로만 쭉 가서는 pac 못감! 왼쪽으로 가다가 위로 갈수있음.
# 한방향의 값만 비교하면 안됨. 따라서 for r in range (x).
# 재귀로 상하좌우 인접한 값은 다 비교해야함.


ROWS, COLM = len(heights), len(heights[0])
pac, atl = set(), set()


def dfs(r, c, visit, pre):
  # 종료조건
  if (r,c) in visit or r<0 or c<0 or r==ROWS or c==COLM or heights[r][c]<pre: return
  visit.add((r,c))
  # 상하좌우 비교
  dfs(r-1,c,visit,heights[r][c])
  dfs(r+1,c,visit,heights[r][c])
  dfs(r,c-1,visit,heights[r][c])
  dfs(r,c+1,visit,heights[r][c])



# pac 왼쪽부터 시작
# atl 오른쪽부터 시작
for r in range(ROWS):
  dfs(r, 0, pac, 0)
  dfs(r, COLM-1, atl, 0)

# pac 위쪽부터 시작
# atl 아래쪽부터 시작
for c in range(COLM):
  dfs(0, c, pac, 0)
  dfs(ROWS-1, c, atl, 0)



# (r,c) pac, atl 모두 도달 가능하면 res에 저장
res=[]
for (r,c) in pac:
  if (r,c) in atl:
    res.append([r,c])