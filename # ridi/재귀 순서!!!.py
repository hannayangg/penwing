# 리턴값을 구하는 재귀 함수
# 호출되는 함수 순서: Fn(5), Fn(4), Fn(3), Fn(2), Fn(1) 종료
# 계산되는 순서: Fn(1), Fn(2), Fn(3), Fn(4), Fn(5)

# 종료조건을 만난 뒤, 호출된 함수 반대방향으로 계산하여 리턴


def Fn(n):
  if n == 1:
    return n
  return n * Fn(n-1)

print(Fn(5))







# 리턴값을 구하지 않는 재귀 함수 (res에 함수인자를 기록하는 게 목적)
# 호출되는 함수 순서: Fn(5), Fn(4), Fn(3), Fn(2), Fn(1) 종료
# res에 저장되는 순서: 1, 2, 3, 4, 5

# 종료조건을 만난 뒤, 호출된 함수 반대 방향으로 저장


res = []

def Fn(n):
  if n == 1:
    res.append(n)
    return
  
  Fn(n-1)
  res.append(n)

print(Fn(5))
print(res)









h = {'A': ['J', 'S'],
     'J': ['A', 'S'],
     'S': ['A']}

# 리턴값을 구하지 않는 재귀 함수 (res에 함수인자를 기록하는 게 목적)
# 호출되는 함수 순서: Fn(J), Fn(A), Fn(J), Fn(S), Fn(A), Fn(S) 종료
# res에 저장되는 순서: S, A, S, J, A, J

# 종료조건을 만난 뒤, 호출된 함수 반대 방향으로 저장

res = []
def Fn(x):
  while h[x]:
    Fn(h[x].pop(0))

  res.append(x)

Fn("J")
print(res)