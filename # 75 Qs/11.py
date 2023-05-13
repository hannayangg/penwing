# [11. leetcode 191]


def F(n):
  return bin(n).count('1')




# 방법1) 1bit 찾는 방법: 101 % 2 = 1.
# 방법2) 1bit 삭제하는 방법: 101 & 100 = 100.