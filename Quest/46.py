# [46. leetcode 54]

# 챗지피티
def F(matrix):
  res = []
  while matrix:
    res += matrix.pop(0)
    if matrix and matrix[0]:
      for row in matrix:
        res.append(row.pop())
    if matrix:
      res += matrix.pop()[::-1]
    if matrix and matrix[0]:
      for row in matrix[::-1]:
        res.append(row.pop(0))
  return res


# 니트코드
def F(matrix):
  L = 0
  R = len(matrix[0])
  T = 0
  B = len(matrix)
  res = []
  
  while L < R and T < B:
    for j in range(L, R):
      res.append(matrix[T][j])
    T += 1
    for i in range(T, B):
      res.append(matrix[i][R-1])
    R -= 1
    if T < B:
      for j in range(R-1, L-1, -1):
        res.append(matrix[B-1][j])
      B -= 1
    if L < R:
      for i in range(B-1, T-1, -1):
        res.append(matrix[i][L])
      L += 1
  return res




# 내가 푼 것
def F(matrix):
  s = 0
  M, N = len(matrix)-1, len(matrix[0])-1
  res = []
  while s < M and s < N:
    for n in range(s, N+1):
      res.append(matrix[s][n])
    for m in range(s+1, M):
      res.append(matrix[m][N])
    for n in range(N, s-1, -1):
      res.append(matrix[M][n])
    for m in range(M-1, s, -1):
      res.append(matrix[m][s])
    s += 1
    M -= 1
    N -= 1    
  # 행또는 열이 하나만 남을 떄
  if s == M:
    for n in range(s, N+1):
      res.append(matrix[s][n])
  elif s == N:
    for m in range(s, M+1):
      res.append(matrix[m][s])
  return res