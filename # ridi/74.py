# [74 1비트의 개수]

# 내가 푼 것. 왜 되는지 모르겠음. 무슨 문젠지 모르겠음.
def F(n):
  return list(bin(n)).count('1')



# 니트코드
# 2로 나눈 나머지 더한 후, 1칸 시프팅 하기.
def F(n):
  res = 0
  while n:
    res += n % 2
    n = n >> 1
  return res

def F(n):
  res = 0
  while n:
    n = n & (n-1)
    res += 1
  return res