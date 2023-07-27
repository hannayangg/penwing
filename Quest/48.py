# [48. leetcode 79]




def F(board, word):
  def dfs(i, j, word):
    if not word: return True
    if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j] != word[0]:
      return False
    
    board[i][j] = ""
    found = dfs(i-1, j, word[1:]) or dfs(i+1, j, word[1:]) or dfs(i, j-1, word[1:]) or dfs(i, j+1, word[1:])
    # 틀린 경로면 원상태로
    board[i][j] = word[0]
    return found

  for col in range(len(board)):
    for row in range(len(board[0])):
      if board[col][row] == word[0] and dfs(col, row, word):
        return True
  return False



# dfs(r, c, i)
# i = word에서의 인덱스.

def F(board, word):
  path = set()
  ROWS, COLS = len(board), len(board[0])

  # i = word에서의 인덱스
  def dfs(r, c, i):
    if i == len(word): return True
    if r<0 or c<0 or r>=ROWS or c>=COLS or board[r][c] != word[i] or (r, c) in path:
      return False
    
    path.add((r, c))
    res = dfs(r-1, c, i+1) or dfs(r+1, c, i+1) or dfs(r, c-1, i+1) or dfs(r, c+1, i+1)
    path.remove((r, c))
    return res
  
  for row in range(ROWS):
    for col in range(COLS):
      if dfs(row, col, 0): return True
  return False
