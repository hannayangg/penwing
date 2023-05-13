# [69 2D 행렬 검색2]

# 내가 푼 것
# 재귀: arr[0][0]에서 시작하여 오른쪽, 아래쪽으로 재귀 호출.
def S(arr, target):
  def F(m, n):
    if m >= len(arr) or n >= len(arr[0]) or arr[m][n] is None:
      return
    if arr[m][n] == target:
      return True
    elif arr[m][n] < target:
      arr[m][n] = None
      if F(m+1, n) or F(m, n+1):
        return True
      return False
  return F(0,0)
# + arr 소트한 후 bisect이용하는 방법도 되었음.


# 책 풀이
# 첫 행의 맨 뒤에서 탐색.

def F(arr, target):
  m = 0
  n = len(arr[0])-1

  while 0 <= m < len(arr) and 0 <= n < len(arr[0]):
    # 개선: n은 항상 작아지는 방향이므로, 음수가 될 가능성은 n만 가짐.
    # while m < len(arr) and 0 <= n:
    if arr[m][n] < target:
      m += 1
    elif arr[m][n] > target:
      n -= 1
    else:
      return True
  return False