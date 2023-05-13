# [47. leetcode 48]


# 왼쪽 대각선 반전, 좌우 반전
def F(matrix):
  n = len(matrix)
  for i in range(n):
    for j in range(i+1, n):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  for row in matrix:
    row.reverse()


# 오른쪽 대각선 반전, 상하 반전
def F(matrix):
  n = len(matrix)-1
  for i in range(n):
    for j in range(n-i):
      matrix[i][j], matrix[n-j][n-i] = matrix[n-j][n-i], matrix[i][j]
  matrix.reverse()


# 4개 스왑
def F(matrix):
  L, R = 0, len(matrix)-1
  n = len(matrix)-1
  for i in range(len(matrix)//2):
    for j in range(L, R):
      matrix[i][j], matrix[j][n-i], matrix[n-i][n-j], matrix[n-j][i] = matrix[n-j][i], matrix[i][j], matrix[j][n-i], matrix[n-i][n-j]
    L += 1
    R -= 1




# 챗지피티
# e-i+s <<= ?

def F(matrix):
    sub_F(matrix, 0, len(matrix) - 1)

def sub_F(matrix, s, e):
    if s >= e: return
    for i in range(s, e):
        tmp = matrix[s][i]
        matrix[s][i] = matrix[e-i+s][s]
        matrix[e-i+s][s] = matrix[e][e-i+s]
        matrix[e][e-i+s] = matrix[i][e]
        matrix[i][e] = tmp
    sub_F(matrix, s+1, e-1)