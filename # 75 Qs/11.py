# [11. leetcode 191]


def F(n):
  return bin(n).count('1')




# 방법1)
# 2로 나눈 나머지를 계속 누적.
# 1011 % 2 = 1 -> 첫번째 비트 1을 찾음.
# 한 칸 오른쪽으로 shift
# 101 % 2 = 0 -> 두번째 비트는 0임을 찾음.
# 한 칸 오른쪽으로 shift 반복

def F(n):
  res = 0
  while n:
    res += n%2
    n = n >> 1
  return res



# 방법2) 1bit 삭제하는 방법: 101 & 100 = 100.